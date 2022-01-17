from rest_framework import serializers
from tickets.models import Ticket


class TicketCreateSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Ticket
        fields = '__all__'