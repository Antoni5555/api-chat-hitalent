from rest_framework import serializers

from .models import Chat, Message

# Минимальная и максимальная длина заголовка чата
CHAT_MIN_LENGTH = 1
CHAT_MAX_LENGTH = 200
# Минимальная и максимальная длина текста сообщения
MESSAGE_MIN_LENGTH = 1
MESSAGE_MAX_LENGTH = 5000


class ChatCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания чата."""

    title = serializers.CharField(
        max_length=CHAT_MAX_LENGTH,
        allow_blank=False,
        trim_whitespace=True,
    )

    class Meta:
        model = Chat
        fields = ('id', 'title', 'created_at')
        read_only_fields = ('id', 'created_at')

    def validate_title(self, value: str) -> str:
        value = value.strip()
        if not CHAT_MIN_LENGTH <= len(value) <= CHAT_MAX_LENGTH:
            raise serializers.ValidationError(
                f'Длина заголовка должна быть от '
                f'{CHAT_MIN_LENGTH} до {CHAT_MAX_LENGTH} символов.'
            )
        return value


class MessageCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для отправки сообщения в чат."""

    text = serializers.CharField(
        max_length=MESSAGE_MAX_LENGTH,
        allow_blank=False,
        trim_whitespace=True,
    )

    class Meta:
        model = Message
        fields = ('id', 'chat', 'text', 'created_at')
        read_only_fields = ('id', 'created_at', 'chat')

    def validate_text(self, value: str) -> str:
        value = value.strip()
        if not MESSAGE_MIN_LENGTH <= len(value) <= MESSAGE_MAX_LENGTH:
            raise serializers.ValidationError(
                f'Длина текста должна быть от '
                f'{MESSAGE_MIN_LENGTH} до {MESSAGE_MAX_LENGTH} символов.'
            )
        return value


class MessageListSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения сообщений."""

    class Meta:
        model = Message
        fields = ('id', 'text', 'created_at')


class ChatDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для получения чата с последними сообщениями."""
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = ('id', 'title', 'created_at', 'messages')

    def get_messages(self, obj):
        limit = self.context.get('limit', 20)
        messages = obj.messages.order_by('-created_at')[:limit]
        return MessageListSerializer(reversed(messages), many=True).data
