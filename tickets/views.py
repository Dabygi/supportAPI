from tickets.models import Ticket, Comment
from tickets.serializers import TicketCreateSerializer, TicketListSerializer, TicketDetailSerializer, \
    CommentCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class TicketCreateView(APIView):
    """Создать тикет"""

    def post(self, request):
        ticket = TicketCreateSerializer(data=request.data)
        if ticket.is_valid():
            ticket.save()
            return Response(status=201)


class TicketListView(APIView):
    """Вывод полного списка тикетов"""

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


