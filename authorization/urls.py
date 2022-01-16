from django.urls import path
from authorization.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]