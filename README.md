# KEYBOARD — Официальный сайт бренда клавиатур

Веб-приложение на **Django** для бренда клавиатур **KEYBOARD**.  
Проект предназначен для демонстрации продукции, управления контентом и дальнейшего развития (каталог, заказы, админ-панель и т.д.).

## Технологический стек

- **Python 3.12**
- **Django**
- **HTML5**/**CSS3**/**JavaScript


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