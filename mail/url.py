from django.urls import path
from . import views

urlpatterns = [
    path('', views.MailAPIView.as_view(), name='home')
]