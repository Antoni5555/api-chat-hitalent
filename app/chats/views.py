from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
)
from rest_framework.mixins import (
    RetrieveModelMixin,
    DestroyModelMixin,
)
from rest_framework.response import Response

from .models import Chat
from .serializers import (
    ChatCreateSerializer,
    ChatDetailSerializer,
    MessageCreateSerializer,
)


class ChatCreateView(CreateAPIView):
    """Создание чата."""

    queryset = Chat.objects.all()
    serializer_class = ChatCreateSerializer


class ChatRetrieveDestroyView(
    RetrieveModelMixin,
    DestroyModelMixin,
    GenericAPIView,
):
    """Получение и удаление чата."""

    queryset = Chat.objects.all()
    serializer_class = ChatDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        chat = self.get_object()
        limit = request.query_params.get('limit', 20)

        try:
            limit = min(int(limit), 100)
        except (TypeError, ValueError):
            limit = 20

        serializer = self.get_serializer(chat, context={'limit': limit})
        return Response(serializer.data)


class MessageCreateView(CreateAPIView):
    """Создание сообщения в чате."""

    serializer_class = MessageCreateSerializer

    def perform_create(self, serializer):
        chat = get_object_or_404(Chat, pk=self.kwargs['pk'])
        serializer.save(chat=chat)
