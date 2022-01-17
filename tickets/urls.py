from django.urls import path
from tickets.views import TicketCreateView

urlpatterns = [
    path('create_ticket/', TicketCreateView.as_view(), name='create_ticket'),
]