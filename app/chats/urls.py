from django.urls import path

from .views import (
    ChatCreateView,
    ChatRetrieveDestroyView,
    MessageCreateView,
)

app_name = 'chats'


urlpatterns = [
    path('chats/', ChatCreateView.as_view(), name='chat-create'),
    path(
        'chats/<int:pk>/',
        ChatRetrieveDestroyView.as_view(),
        name='chat-detail'),
    path(
        'chats/<int:pk>/messages/',
        MessageCreateView.as_view(),
        name='message-create',),
]
