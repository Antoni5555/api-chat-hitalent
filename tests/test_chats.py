import pytest
from django.urls import reverse


DEFAULT_LIMIT = 20                  # Кол-во сообщений по умолчанию
CUSTOM_LIMIT = 5                    # Пример лимита сообщений
EXCEEDED_LIMIT = 999                # Лимит для проверки ограничения
INVALID_TITLES = ['', '   ', None]  # Некорректные заголовки чата
CHAT_TITLE = 'Мой первый чат'       # Тестовый корректный заголовок


pytestmark = pytest.mark.django_db


def test_create_chat(api_client):
    """Создание нового чата должно возвращать 201 и корректные данные."""
    url = reverse('chats:chat-create')
    data = {'title': CHAT_TITLE}

    response = api_client.post(url, data=data, format='json')

    assert response.status_code == 201
    assert response.data['title'] == CHAT_TITLE
    assert 'id' in response.data


@pytest.mark.parametrize('title', INVALID_TITLES)
def test_create_chat_validation_error(api_client, title):
    """Создание чата с пустым/некорректным заголовком возвращает 400."""
    url = reverse('chats:chat-create')
    data = {'title': title}

    response = api_client.post(url, data=data, format='json')

    assert response.status_code == 400


def test_get_chat_with_messages(api_client, chat, messages):
    """
    Получение чата должно возвращать
    последние DEFAULT_LIMIT сообщений по-умолчанию.
    """
    url = reverse('chats:chat-detail', kwargs={'pk': chat.id})

    response = api_client.get(url)

    assert response.status_code == 200
    assert response.data['id'] == chat.id
    assert len(response.data['messages']) == DEFAULT_LIMIT


def test_get_chat_with_custom_limit(api_client, chat, messages):
    """Получение чата с лимитом должно возвращать заданное кол-во сообщений."""
    url = reverse('chats:chat-detail', kwargs={'pk': chat.id})

    response = api_client.get(url, {'limit': CUSTOM_LIMIT})

    assert response.status_code == 200
    assert len(response.data['messages']) == CUSTOM_LIMIT


def test_get_chat_limit_cannot_exceed_100(api_client, chat, messages):
    """Если запрошен лимит выше 100, возвращаются все доступные сообщения."""
    url = reverse('chats:chat-detail', kwargs={'pk': chat.id})

    response = api_client.get(url, {'limit': EXCEEDED_LIMIT})

    assert response.status_code == 200
    assert len(response.data['messages']) == len(messages)


def test_delete_chat(api_client, chat):
    """Удаление чата должно возвращать статус 204 и удалять чат из базы."""
    url = reverse('chats:chat-detail', kwargs={'pk': chat.id})

    response = api_client.delete(url)

    assert response.status_code == 204


def test_get_deleted_chat_returns_404(api_client, chat):
    """После удаления чата попытка получить его должна вернуть 404."""
    url = reverse('chats:chat-detail', kwargs={'pk': chat.id})

    api_client.delete(url)
    response = api_client.get(url)

    assert response.status_code == 404
