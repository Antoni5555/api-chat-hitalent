import pytest
from django.urls import reverse


MESSAGE_TEXT = 'Привет! Мой друг.'          # Тестовый текст сообщения
INVALID_TEXTS = ['', '   ', None]     # Некорректные тексты сообщений
NONEXISTENT_CHAT_ID = 9999            # ID несуществующего чата для теста 404

pytestmark = pytest.mark.django_db


def test_create_message(api_client, chat):
    """
    Создание сообщения в существующем чате
    должно вернуть 201 и корректные данные.
    """
    url = reverse('chats:message-create', kwargs={'pk': chat.id})
    data = {'text': MESSAGE_TEXT}

    response = api_client.post(url, data=data, format='json')

    assert response.status_code == 201
    assert response.data['text'] == MESSAGE_TEXT
    assert 'id' in response.data


def test_create_message_for_nonexistent_chat(api_client):
    """Попытка создать сообщение в несуществующем чате должна вернуть 404."""
    url = reverse('chats:message-create', kwargs={'pk': NONEXISTENT_CHAT_ID})
    data = {'text': MESSAGE_TEXT}

    response = api_client.post(url, data=data, format='json')

    assert response.status_code == 404


@pytest.mark.parametrize('text', INVALID_TEXTS)
def test_message_text_validation(api_client, chat, text):
    """
    Попытка создать сообщение с пустым
    или некорректным текстом должна вернуть 400.
    """
    url = reverse('chats:message-create', kwargs={'pk': chat.id})
    data = {'text': text}

    response = api_client.post(url, data=data, format='json')

    assert response.status_code == 400
