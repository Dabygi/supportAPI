import os
import jwt
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import generics, status, views
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from authorization.models import User
from authorization.serializers import LoginSerializer
from rest_framework.permissions import AllowAny
from authorization.serializers import RegisterSerializer, EmailVerificationSerializer
from authorization.tasks import send_activation_email
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data  # переменная хранит данные пользовательского запроса.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        current_site = get_current_site(request).domain
        token = RefreshToken.for_user(user).access_token

        email_subject = 'Verify your email'
        email_body = f"Hi {serializer.validated_data.get('username')}. Use link for verify your email." \
                     f"http://{current_site}/authentication/verify-email/?token={str(token)}"
        send_activation_email.delay(email_subject, email_body, settings.EMAIL_HOST_USER,
                                    serializer.validated_data.get('email'))

        return Response(user_data, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        user = get_object_or_404(User, email=request.data['email'])
        token = str(RefreshToken.for_user(user).access_token)
        return Response({'token': token}, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializer

    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': "Activation Expired"}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as decodeError:
            return Response({'error': "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
