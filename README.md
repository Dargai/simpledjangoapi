# 📚 Simple Django REST API — CRUD Course Project

A beginner-friendly REST API built with **Django** and **Django REST Framework (DRF)**.
This project exposes a full CRUD interface for an online course catalog, letting you create, read, update and delete courses via standard HTTP methods (GET, POST, PUT, DELETE).

> **Goal of this guide:** Understand what Django REST Framework is, how it works, and walk through every step — from environment setup to pushing your project to GitHub.

---

## 🗂️ Table of Contents

1. [What is Django REST Framework?](#1-what-is-django-rest-framework)
2. [Prerequisites & Tools](#2-prerequisites--tools)
3. [Environment Setup](#3-environment-setup)
4. [Installing Django & DRF](#4-installing-django--drf)
5. [Creating the Django Project](#5-creating-the-django-project)
6. [Creating the App](#6-creating-the-app)
7. [Configuring `settings.py`](#7-configuring-settingspy)
8. [Running Migrations & the Server](#8-running-migrations--the-server)
9. [Django Admin Area](#9-django-admin-area)
10. [Creating the Model](#10-creating-the-model)
11. [Creating the Serializer](#11-creating-the-serializer)
12. [Creating the View](#12-creating-the-view)
13. [Configuring URLs & Routes](#13-configuring-urls--routes)
14. [Testing the API](#14-testing-the-api)
15. [Pushing to GitHub](#15-pushing-to-github)

---

## 1. What is Django REST Framework?

**Django** is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

**Django REST Framework (DRF)** is a powerful toolkit built on top of Django that makes it easy to build Web APIs. It provides:

- **Serializers** — convert Python objects (models) to JSON and back
- **ViewSets** — class-based views that handle all CRUD operations automatically
- **Routers** — automatically wire HTTP methods (GET, POST, PUT, DELETE) to URLs
- **A browsable API** — a built-in web interface to explore and test your API in the browser

The typical flow of a DRF request looks like this:

```
HTTP Request → URL Router → ViewSet → Serializer → Model (Database)
                                                         ↕
HTTP Response ← URL Router ← ViewSet ← Serializer ← Model (Database)
```

---

## 2. Prerequisites & Tools

Before starting, make sure you have the following installed on your machine:

| Tool | Purpose | Download |
|---|---|---|
| **Python 3.10+** | Runtime | [python.org](https://www.python.org/downloads/) |
| **pip** | Python package manager | Comes with Python |
| **VS Code** or **Sublime Text** | Code editor | [code.visualstudio.com](https://code.visualstudio.com/) |
| **Git Bash** (Windows) | Terminal emulator | [git-scm.com](https://git-scm.com/) |
| **Git** | Version control | [git-scm.com](https://git-scm.com/) |

> 💡 **Windows users using Git Bash:** Some Python commands require the `winpty` prefix to work correctly in Git Bash (e.g., `winpty python manage.py runserver`). This guide will flag every place this applies.

---

## 3. Environment Setup

### 3.1 — Create your project folder

```bash
mkdir djangoapi
cd djangoapi
```

### 3.2 — Create a virtual environment

A virtual environment keeps your project's dependencies isolated from the rest of your system.

```bash
python -m venv my_venv
```

### 3.3 — Activate the virtual environment

| Platform | Command |
|---|---|
| **Windows (Git Bash)** | `source my_venv/Scripts/activate` |
| **macOS / Linux** | `source my_venv/bin/activate` |

Once activated, your terminal prompt will show `(my_venv)` at the beginning — that confirms the environment is active.

### 3.4 — Verify the environment

```bash
pip freeze
```

This lists all installed packages. Inside a fresh virtual environment, it should return nothing (or very little).

### 3.5 — Deactivate when done

```bash
deactivate
```

---

## 4. Installing Django & DRF

Make sure your virtual environment is **active** before running these commands.

```bash
pip install Django
pip install djangorestframework
```

After installation, `pip freeze` should show something like:

```
asgiref==3.11.1
Django==6.0.3
djangorestframework==3.16.1
sqlparse==0.5.5
tzdata==2025.3
```

> The versions you see may differ — that is normal.

---

## 5. Creating the Django Project

### 5.1 — Start the project

```bash
django-admin startproject djangoapi .
```

> The trailing `.` creates the project in the current folder instead of creating a nested subfolder. This keeps the structure clean.

### 5.2 — Understand the generated structure

```
djangoapi/
├── manage.py          ← entry point for all Django commands
└── djangoapi/
    ├── __init__.py
    ├── settings.py    ← project configuration
    ├── urls.py        ← global URL routing
    ├── asgi.py
    └── wsgi.py
```

> ⚠️ **Always run Django commands from the folder that contains `manage.py`.**

---

## 6. Creating the App

A Django **project** can contain multiple **apps**. Each app handles a specific feature. Here we create a `courses` app.

```bash
python manage.py startapp courses
```

This generates the following structure inside your project:

```
courses/
├── admin.py
├── apps.py
├── models.py       ← define your data models here
├── serializers.py  ← you will create this file
├── urls.py         ← you will create this file
├── views.py
└── migrations/
```

---

## 7. Configuring `settings.py`

Open `djangoapi/settings.py` and add `rest_framework` and your new app to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',

    # Your apps
    'courses',
]
```

---

## 8. Running Migrations & the Server

Django ships with a built-in database (SQLite) and some pre-built models (users, admin, etc.). You need to apply these before anything works.

### 8.1 — Apply initial migrations

| Platform | Command |
|---|---|
| **macOS / Linux** | `python manage.py migrate` |
| **Windows (Git Bash)** | `winpty python manage.py migrate` |

### 8.2 — Start the development server

| Platform | Command |
|---|---|
| **macOS / Linux** | `python manage.py runserver` |
| **Windows (Git Bash)** | `winpty python manage.py runserver` |

Open your browser and go to **[http://localhost:8000](http://localhost:8000)**. You should see the Django welcome page. 🎉

---

## 9. Django Admin Area

Django provides a built-in admin panel at `http://localhost:8000/admin/` where you can manage your database records directly from the browser.

### 9.1 — Create a superuser (admin account)

| Platform | Command |
|---|---|
| **macOS / Linux** | `python manage.py createsuperuser` |
| **Windows (Git Bash)** | `winpty python manage.py createsuperuser` |

Follow the prompts to set a username, email, and password.

### 9.2 — Access the admin panel

Restart the server and go to `http://localhost:8000/admin/`, then log in with your credentials.

---

## 10. Creating the Model

A **Model** is a Python class that represents a database table. Each attribute becomes a column.

### 10.1 — Define the `Course` model

Edit `courses/models.py`:

```python
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name  # Shows course name instead of "Course object (1)" in admin
```

### 10.2 — Create and apply migrations

Every time you create or modify a model, you must run two commands:

```bash
# Generate the migration file
python manage.py makemigrations

# Apply it to the database
python manage.py migrate
```

> **Git Bash on Windows:** prefix both with `winpty`.

### 10.3 — Register the model in the Admin panel

Edit `courses/admin.py`:

```python
from django.contrib import admin
from .models import Course

admin.site.register(Course)
```

You can now add, edit and delete courses directly from `http://localhost:8000/admin/`.

---

## 11. Creating the Serializer

A **Serializer** converts a `Course` object into JSON (for sending to the client) and converts incoming JSON back into a `Course` object (for saving to the database).

Create a new file `courses/serializers.py`:

```python
from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'url', 'name', 'language', 'price')
```

> `HyperlinkedModelSerializer` adds a `url` field that acts as a clickable link to each course resource — making the API easier to navigate.

---

## 12. Creating the View

A **ViewSet** bundles all the CRUD logic (list, create, retrieve, update, destroy) into a single class. DRF handles the rest automatically.

Edit `courses/views.py`:

```python
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()       # Fetch all courses from the database
    serializer_class = CourseSerializer   # Use our serializer to format the data
```

---

## 13. Configuring URLs & Routes

### 13.1 — Create `courses/urls.py`

The `courses` app does not have a `urls.py` by default — you need to create it:

```python
from django.urls import path, include
from rest_framework import routers
from . import views

# A router automatically creates URLs for all CRUD operations
router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

The router maps the following routes automatically:

| HTTP Method | URL | Action |
|---|---|---|
| GET | `/courses/` | List all courses |
| POST | `/courses/` | Create a new course |
| GET | `/courses/{id}/` | Retrieve a single course |
| PUT | `/courses/{id}/` | Update a course |
| DELETE | `/courses/{id}/` | Delete a course |

### 13.2 — Register the app URLs in the global `urls.py`

Edit `djangoapi/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),  # '' means root — accessible at localhost:8000/courses/
]
```

---

## 14. Testing the API

### Option A — Browsable API (built into DRF)

Go to **[http://localhost:8000/courses/](http://localhost:8000/courses/)** in your browser. DRF renders a human-friendly interface where you can read and post data without any extra tools.

### Option B — Postman or Insomnia

Download [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/) and send requests manually:

```
GET    http://localhost:8000/courses/
POST   http://localhost:8000/courses/        Body: {"name": "Python", "language": "Python", "price": "29.99"}
PUT    http://localhost:8000/courses/1/      Body: {"name": "Python Pro", "language": "Python", "price": "49.99"}
DELETE http://localhost:8000/courses/1/
```

### Option C — curl (terminal)

```bash
# List all courses
curl http://localhost:8000/courses/

# Create a course
curl -X POST http://localhost:8000/courses/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Python Basics", "language": "Python", "price": "19.99"}'
```

---

## 15. Pushing to GitHub

### 15.1 — Create a `.gitignore` file

Before committing, create a `.gitignore` file in your root folder to exclude files that should not be tracked:

```
# Virtual environment
my_venv/

# Python cache
__pycache__/
*.pyc
*.pyo

# Django
*.sqlite3
*.log

# VS Code
.vscode/
```

### 15.2 — Initialize Git and make the first commit

```bash
git init
git add .
git commit -m "Initial commit: Django REST API CRUD for courses"
```

### 15.3 — Connect to GitHub and push

```bash
git remote add origin https://github.com/Dargai/simpledjangoapi.git
git branch -M main
git push -u origin main
```

> After the first push, you can simply use `git push` for future commits.

### 15.4 — Typical workflow after changes

```bash
git add .
git commit -m "describe what you changed"
git push
```

---

## 📁 Final Project Structure

```
djangoapi/
├── .gitignore
├── manage.py
├── djangoapi/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── courses/
    ├── admin.py
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── migrations/
```

---

## 📌 Quick Command Reference

| Action | macOS / Linux | Windows Git Bash |
|---|---|---|
| Activate venv | `source my_venv/bin/activate` | `source my_venv/Scripts/activate` |
| Run migrations | `python manage.py migrate` | `winpty python manage.py migrate` |
| Make migrations | `python manage.py makemigrations` | `winpty python manage.py makemigrations` |
| Start server | `python manage.py runserver` | `winpty python manage.py runserver` |
| Create superuser | `python manage.py createsuperuser` | `winpty python manage.py createsuperuser` |
| Start new app | `python manage.py startapp appname` | `winpty python manage.py startapp appname` |

---

*Built with ❤️ using Django & Django REST Framework*
