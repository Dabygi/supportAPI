from rest_framework import generics
from tickets.serializers import TicketCreateSerializer


class TicketCreateView(generics.CreateAPIView):
    serializer_class = TicketCreateSerializer