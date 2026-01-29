from django.db import models


class Chat(models.Model):
    """Модель чата(заголовок/время создания)."""

    title = models.CharField(
        max_length=200,
        blank=False,
    )
    created_at = models.DateTimeField(auto_now_add=True,)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f'Chat(id={self.id}, title={self.title})'


class Message(models.Model):
    """Модель сообщения связанного с чатом(текст/время создания)."""

    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name='messages',
    )
    text = models.TextField(blank=False,)
    created_at = models.DateTimeField(auto_now_add=True,)

    class Meta:
        ordering = ['created_at']

    def __str__(self) -> str:
        return f'Message(id={self.id}, chat_id={self.chat_id})'
