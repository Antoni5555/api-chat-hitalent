import pytest
from rest_framework.test import APIClient

from chats.models import Chat, Message


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def chat():
    return Chat.objects.create(title='Test chat')


@pytest.fixture
def messages(chat):
    msgs = [
        Message.objects.create(chat=chat, text=f'msg {i}')
        for i in range(30)
    ]
    return msgs
