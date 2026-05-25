# Django Project Setup Guide

## Create Project

### 1. Create project folder

```bash
mkdir DjangoProject
cd DjangoProject
```

### 2. Create virtual environment

```bash
python -m venv env
```

Purpose:
- Creates an isolated Python environment
- Avoids package conflicts

### 3. Activate virtual environment

Windows:

```bash
.\env\Scripts\activate
```

Linux / Mac:

```bash
source env/bin/activate
```

After activation:

```bash
(env)
```

will appear in terminal.

### 4. Install Django

```bash
pip install django
```

Check Django version:

```bash
python -m django --version
```

### 5. Create Django project

```bash
django-admin startproject project_name .
```

`.` means create project inside current folder.

### 6. Run server

```bash
python manage.py runserver
```

Default URL:

```text
http://127.0.0.1:8000/
```

Custom port:

```bash
python manage.py runserver 8001
```

---

# Django Useful Commands

## Create app

```bash
python manage.py startapp app_name
```

Example:

```bash
python manage.py startapp store
```

Purpose:
- Creates a Django application

---

## Make migrations

```bash
python manage.py makemigrations
```

Purpose:
- Detects model changes

---

## Apply migrations

```bash
python manage.py migrate
```

Purpose:
- Applies database changes

Flow:

```text
Model → Migration → Database
```

---

## Create admin user

```bash
python manage.py createsuperuser
```

Purpose:
- Creates admin panel account

---

## Open Django shell

```bash
python manage.py shell
```

Example:

```python
from store.models import Product

Product.objects.all()
```

---

## Show SQL queries

```bash
python manage.py sqlmigrate app_name migration_number
```

Example:

```bash
python manage.py sqlmigrate store 0001
```

---

## Collect static files

```bash
python manage.py collectstatic
```

Purpose:
- Collect CSS, JS, images for production

---

# Django Request Flow

```text
Browser Request
        ↓
      URL
        ↓
      View
        ↓
     Model
        ↓
    Database
        ↓
    Template
        ↓
    Response
```

Example:

views.py

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World")
```

urls.py

```python
from django.urls import path
from .views import home

urlpatterns = [
    path('', home)
]
```

Result:

```text
http://127.0.0.1:8000/

Hello World
```

---

# Project Structure

```text
project/
│
├── manage.py
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── migrations/
│
├── templates/
├── static/
└── media/
```

### File Purpose

- manage.py → Execute Django commands
- settings.py → Project settings
- urls.py → URL routes
- views.py → Business logic
- models.py → Database tables
- admin.py → Admin panel configuration
- templates → HTML files
- static → CSS/JS/images
- media → User uploaded files
