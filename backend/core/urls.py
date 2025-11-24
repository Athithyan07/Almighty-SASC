from django.urls import path
from . import views

urlpatterns = [
    path('chat/history/', views.get_chat_history, name='chat_history'),
    path('chat/send/', views.send_chat_message, name='send_chat_message'),
]