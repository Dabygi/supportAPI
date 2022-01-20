from rest_framework import serializers
from authorization.models import User
from django.core import exceptions
import django.contrib.auth.password_validation as validators


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'confirm_password']

    def validate(self, attrs):
        password = attrs.get('password', '')
        confirm_password = attrs.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Пароли не совпадают!!!',
                                               'confirm_password': 'Пароли не совпадают!!!'})
        try:
            validators.validate_password(password=password)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})

        attrs.pop('confirm_password', None)
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create(**validated_data)