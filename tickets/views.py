from django.contrib.sites.shortcuts import get_current_site
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from tickets.models import Ticket
from tickets.serializers import TicketCreateSerializer, TicketListSerializer, TicketDetailSerializer, \
    CommentCreateSerializer


class TicketCreateView(APIView):
    """Создать тикет"""

    def post(self, request):
        ticket = TicketCreateSerializer(data=request.data)
        if ticket.is_valid():
            ticket.save()
            return Response(status=201)


class TicketListView(APIView):
    """Вывод полного списка тикетов"""

    permission_classes = (AllowAny,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'subcategory', 'ticket_status']

    def get(self, request):
        tickets = Ticket.objects.all()
        serializer = TicketListSerializer(tickets, many=True)
        return Response(serializer.data)


class TicketDetailView(APIView):
    """Вывод конкретного тикета"""

    def get(self, request, pk):
        tickets = Ticket.objects.get(id=pk)
        serializer = TicketDetailSerializer(tickets)
        return Response(serializer.data)


class CommentCreateView(APIView):
    """Добавление комментария"""

    def post(self, request):
        comment = CommentCreateSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
            return Response(status=201)


