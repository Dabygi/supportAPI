from rest_framework import serializers
from tickets.models import Ticket, Comment


class CommentCreateSerializer(serializers.ModelSerializer):
    """Создать комментарий"""

    class Meta:
        model = Comment
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):
    """Вывод комментариев"""
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    ticket = serializers.SlugRelatedField(slug_field='text', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class TicketCreateSerializer(serializers.ModelSerializer):
    """Создать тикет"""

    class Meta:
        model = Ticket
        exclude = ('author', 'responsible')


class TicketListSerializer(serializers.ModelSerializer):
    """Список тикетов"""
    category = serializers.SlugRelatedField(slug_field='category', read_only=True)
    subcategory = serializers.SlugRelatedField(slug_field='subcategory', read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    responsible = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Ticket
        fields = ('author', 'responsible', 'ticket_status', 'category', 'subcategory')


class TicketDetailSerializer(serializers.ModelSerializer):
    """Полный тикет"""
    category = serializers.SlugRelatedField(slug_field='category', read_only=True)
    subcategory = serializers.SlugRelatedField(slug_field='subcategory', read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    responsible = serializers.SlugRelatedField(slug_field='username', read_only=True)
    comments = CommentListSerializer(many=True)

    class Meta:
        model = Ticket
        fields = '__all__'