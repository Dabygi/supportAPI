from django.contrib.sites.shortcuts import get_current_site
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from tickets.models import Ticket
from tickets.serializers import TicketCreateSerializer, TicketListSerializer, TicketDetailSerializer, \
    CommentCreateSerializer


class TicketCreateView(generics.CreateAPIView):
    """Создать тикет"""

    serializer_class = TicketCreateSerializer
    permission_classes = (AllowAny,)


class TicketListView(generics.ListAPIView):
    """Вывод полного списка тикетов"""

    serializer_class = TicketListSerializer
    permission_classes = (AllowAny,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'subcategory', 'ticket_status']

    def get_queryset(self):
        tickets = Ticket.objects.all()
        return tickets


class TicketDetailView(generics.RetrieveAPIView):
    """Вывод конкретного тикета"""

    serializer_class = TicketDetailSerializer
    queryset = Ticket.objects.filter()


class CommentCreateView(generics.CreateAPIView):
    """Добавление комментария"""

    serializer_class = CommentCreateSerializer


