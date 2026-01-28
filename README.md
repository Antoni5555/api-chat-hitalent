# Chat API — REST API для чатов и сообщений

Простой веб-сервис на **Django + DRF** для работы с чатами и сообщениями.  
Позволяет создавать чаты, отправлять сообщения, получать чат с последними сообщениями и удалять чаты вместе с их сообщениями.

## Технологический стек

- **Python 3.12**
- **Django 5**
- **Django REST Framework**
- **PostgreSQL**
- **Docker + docker-compose**
- **pytest**


## Установка и запуск проекта

### 1. Создание и активация виртуального окружения
```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Обновление pip и установка зависимостей
```bash
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Создание Django-проекта
```bash
django-admin startproject app
cd app

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```