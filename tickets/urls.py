from django.urls import path
from tickets.views import TicketCreateView, TicketListView, TicketDetailView, CommentCreateView

urlpatterns = [
    path('create_ticket/', TicketCreateView.as_view(), name='create_ticket'),
    path('ticket/', TicketListView.as_view(), name='all_tickets'),
    path('ticket/<int:pk>/', TicketDetailView.as_view(), name='ticket_by_id'),

    path('comment/', CommentCreateView.as_view(), name='create_comment'),
]