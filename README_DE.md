# 📚 Simple Django REST API — CRUD Kursprojekt

Eine anfängerfreundliche REST API, erstellt mit **Django** und **Django REST Framework (DRF)**.
Dieses Projekt stellt eine vollständige CRUD-Schnittstelle für einen Online-Kurskatalog bereit und ermöglicht das Erstellen, Lesen, Aktualisieren und Löschen von Kursen über Standard-HTTP-Methoden (GET, POST, PUT, DELETE).

> **Ziel dieser Anleitung:** Verstehen, was Django REST Framework ist, wie es funktioniert, und jeden Schritt nachvollziehen — von der Einrichtung der Umgebung bis zum Hochladen auf GitHub.

---

## 🗂️ Inhaltsverzeichnis

1. [Was ist Django REST Framework?](#1-was-ist-django-rest-framework)
2. [Voraussetzungen & Werkzeuge](#2-voraussetzungen--werkzeuge)
3. [Umgebung einrichten](#3-umgebung-einrichten)
4. [Django & DRF installieren](#4-django--drf-installieren)
5. [Das Django-Projekt erstellen](#5-das-django-projekt-erstellen)
6. [Die App erstellen](#6-die-app-erstellen)
7. [`settings.py` konfigurieren](#7-settingspy-konfigurieren)
8. [Migrationen & Server starten](#8-migrationen--server-starten)
9. [Django-Administrationsbereich](#9-django-administrationsbereich)
10. [Das Modell erstellen](#10-das-modell-erstellen)
11. [Den Serializer erstellen](#11-den-serializer-erstellen)
12. [Den View erstellen](#12-den-view-erstellen)
13. [URLs & Routen konfigurieren](#13-urls--routen-konfigurieren)
14. [Die API testen](#14-die-api-testen)
15. [Projekt auf GitHub hochladen](#15-projekt-auf-github-hochladen)

---

## 1. Was ist Django REST Framework?

**Django** ist ein leistungsstarkes Python-Webframework, das schnelle Entwicklung und sauberes, pragmatisches Design fördert.

**Django REST Framework (DRF)** ist ein umfangreiches Toolkit, das auf Django aufbaut und die Erstellung von Web-APIs erheblich vereinfacht. Es bietet:

- **Serializer** — wandeln Python-Objekte (Modelle) in JSON um und umgekehrt
- **ViewSets** — klassenbasierte Views, die alle CRUD-Operationen automatisch verwalten
- **Router** — verknüpfen HTTP-Methoden (GET, POST, PUT, DELETE) automatisch mit URLs
- **Eine durchsuchbare API** — eine eingebaute Weboberfläche zum Erkunden und Testen der API direkt im Browser

Der typische Ablauf einer DRF-Anfrage sieht so aus:

```
HTTP-Anfrage → URL-Router → ViewSet → Serializer → Modell (Datenbank)
                                                          ↕
HTTP-Antwort ← URL-Router ← ViewSet ← Serializer ← Modell (Datenbank)
```

---

## 2. Voraussetzungen & Werkzeuge

Stellen Sie sicher, dass folgende Programme auf Ihrem Rechner installiert sind:

| Werkzeug | Zweck | Download |
|---|---|---|
| **Python 3.10+** | Laufzeitumgebung | [python.org](https://www.python.org/downloads/) |
| **pip** | Python-Paketverwaltung | Wird mit Python mitgeliefert |
| **VS Code** oder **Sublime Text** | Code-Editor | [code.visualstudio.com](https://code.visualstudio.com/) |
| **Git Bash** (Windows) | Terminal-Emulator | [git-scm.com](https://git-scm.com/) |
| **Git** | Versionskontrolle | [git-scm.com](https://git-scm.com/) |

> 💡 **Windows-Nutzer mit Git Bash:** Einige Python-Befehle benötigen das Präfix `winpty`, um in Git Bash korrekt zu funktionieren (z. B. `winpty python manage.py runserver`). Diese Anleitung weist an jeder entsprechenden Stelle darauf hin.

---

## 3. Umgebung einrichten

### 3.1 — Projektordner erstellen

```bash
mkdir djangoapi
cd djangoapi
```

### 3.2 — Virtuelle Umgebung erstellen

Eine virtuelle Umgebung hält die Abhängigkeiten Ihres Projekts vom Rest des Systems isoliert.

```bash
python -m venv my_venv
```

### 3.3 — Virtuelle Umgebung aktivieren

| Plattform | Befehl |
|---|---|
| **Windows (Git Bash)** | `source my_venv/Scripts/activate` |
| **macOS / Linux** | `source my_venv/bin/activate` |

Nach der Aktivierung zeigt das Terminal `(my_venv)` am Anfang der Zeile — das bestätigt, dass die Umgebung aktiv ist.

### 3.4 — Umgebung überprüfen

```bash
pip freeze
```

Dieser Befehl listet alle installierten Pakete auf. In einer frischen virtuellen Umgebung sollte er nichts (oder kaum etwas) zurückgeben.

### 3.5 — Umgebung deaktivieren

```bash
deactivate
```

---

## 4. Django & DRF installieren

Stellen Sie sicher, dass Ihre virtuelle Umgebung **aktiv** ist, bevor Sie diese Befehle ausführen.

```bash
pip install Django
pip install djangorestframework
```

Nach der Installation sollte `pip freeze` in etwa Folgendes anzeigen:

```
asgiref==3.11.1
Django==6.0.3
djangorestframework==3.16.1
sqlparse==0.5.5
tzdata==2025.3
```

> Die angezeigten Versionsnummern können abweichen — das ist völlig normal.

---

## 5. Das Django-Projekt erstellen

### 5.1 — Projekt starten

```bash
django-admin startproject djangoapi .
```

> Der abschließende `.` erstellt das Projekt im aktuellen Ordner, anstatt einen verschachtelten Unterordner anzulegen. Das sorgt für eine übersichtlichere Struktur.

### 5.2 — Die generierte Struktur verstehen

```
djangoapi/
├── manage.py          ← Einstiegspunkt für alle Django-Befehle
└── djangoapi/
    ├── __init__.py
    ├── settings.py    ← Projektkonfiguration
    ├── urls.py        ← Globales URL-Routing
    ├── asgi.py
    └── wsgi.py
```

> ⚠️ **Führen Sie Django-Befehle immer aus dem Ordner aus, der `manage.py` enthält.**

---

## 6. Die App erstellen

Ein Django-**Projekt** kann mehrere **Apps** enthalten. Jede App verwaltet eine bestimmte Funktion. Hier erstellen wir eine `courses`-App.

```bash
python manage.py startapp courses
```

Dadurch wird folgende Struktur innerhalb Ihres Projekts generiert:

```
courses/
├── admin.py
├── apps.py
├── models.py       ← Hier definieren Sie Ihre Datenmodelle
├── serializers.py  ← Diese Datei erstellen Sie selbst
├── urls.py         ← Diese Datei erstellen Sie selbst
├── views.py
└── migrations/
```

---

## 7. `settings.py` konfigurieren

Öffnen Sie `djangoapi/settings.py` und fügen Sie `rest_framework` sowie Ihre neue App zu `INSTALLED_APPS` hinzu:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Drittanbieter-Bibliotheken
    'rest_framework',

    # Eigene Apps
    'courses',
]
```

---

## 8. Migrationen & Server starten

Django wird mit einer eingebauten Datenbank (SQLite) und einigen vorgefertigten Modellen (Benutzer, Admin usw.) geliefert. Diese müssen angewendet werden, bevor irgendetwas funktioniert.

### 8.1 — Initiale Migrationen anwenden

| Plattform | Befehl |
|---|---|
| **macOS / Linux** | `python manage.py migrate` |
| **Windows (Git Bash)** | `winpty python manage.py migrate` |

### 8.2 — Entwicklungsserver starten

| Plattform | Befehl |
|---|---|
| **macOS / Linux** | `python manage.py runserver` |
| **Windows (Git Bash)** | `winpty python manage.py runserver` |

Öffnen Sie Ihren Browser und rufen Sie **[http://localhost:8000](http://localhost:8000)** auf. Sie sollten die Django-Willkommensseite sehen. 🎉

---

## 9. Django-Administrationsbereich

Django stellt unter `http://localhost:8000/admin/` ein eingebautes Verwaltungspanel bereit, über das Sie Datenbankeinträge direkt im Browser verwalten können.

### 9.1 — Superuser (Administrator-Konto) erstellen

| Plattform | Befehl |
|---|---|
| **macOS / Linux** | `python manage.py createsuperuser` |
| **Windows (Git Bash)** | `winpty python manage.py createsuperuser` |

Folgen Sie den Anweisungen, um Benutzername, E-Mail und Passwort festzulegen.

### 9.2 — Auf den Administrationsbereich zugreifen

Starten Sie den Server neu und rufen Sie `http://localhost:8000/admin/` auf. Melden Sie sich mit Ihren Zugangsdaten an.

---

## 10. Das Modell erstellen

Ein **Modell** ist eine Python-Klasse, die eine Datenbanktabelle repräsentiert. Jedes Attribut wird zu einer Spalte.

### 10.1 — Das `Course`-Modell definieren

Bearbeiten Sie `courses/models.py`:

```python
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name  # Zeigt den Kursnamen statt "Course object (1)" im Admin-Bereich
```

### 10.2 — Migrationen erstellen und anwenden

Jedes Mal, wenn Sie ein Modell erstellen oder ändern, müssen Sie zwei Befehle ausführen:

```bash
# Migrationsdatei generieren
python manage.py makemigrations

# Auf die Datenbank anwenden
python manage.py migrate
```

> **Git Bash unter Windows:** Fügen Sie `winpty` vor beiden Befehlen hinzu.

### 10.3 — Das Modell im Administrationsbereich registrieren

Bearbeiten Sie `courses/admin.py`:

```python
from django.contrib import admin
from .models import Course

admin.site.register(Course)
```

Sie können nun Kurse direkt über `http://localhost:8000/admin/` hinzufügen, bearbeiten und löschen.

---

## 11. Den Serializer erstellen

Ein **Serializer** wandelt ein `Course`-Objekt in JSON um (zum Senden an den Client) und konvertiert eingehendes JSON zurück in ein `Course`-Objekt (zum Speichern in der Datenbank).

Erstellen Sie eine neue Datei `courses/serializers.py`:

```python
from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'url', 'name', 'language', 'price')
```

> `HyperlinkedModelSerializer` fügt ein `url`-Feld hinzu, das als anklickbarer Link zu jeder Kursressource dient — das macht die API einfacher navigierbar.

---

## 12. Den View erstellen

Ein **ViewSet** bündelt die gesamte CRUD-Logik (auflisten, erstellen, abrufen, aktualisieren, löschen) in einer einzigen Klasse. DRF erledigt den Rest automatisch.

Bearbeiten Sie `courses/views.py`:

```python
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()       # Alle Kurse aus der Datenbank abrufen
    serializer_class = CourseSerializer   # Unseren Serializer zur Datenformatierung verwenden
```

---

## 13. URLs & Routen konfigurieren

### 13.1 — `courses/urls.py` erstellen

Die `courses`-App hat standardmäßig keine `urls.py` — Sie müssen sie selbst erstellen:

```python
from django.urls import path, include
from rest_framework import routers
from . import views

# Ein Router erstellt automatisch URLs für alle CRUD-Operationen
router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

Der Router verknüpft automatisch folgende Routen:

| HTTP-Methode | URL | Aktion |
|---|---|---|
| GET | `/courses/` | Alle Kurse auflisten |
| POST | `/courses/` | Neuen Kurs erstellen |
| GET | `/courses/{id}/` | Einen Kurs abrufen |
| PUT | `/courses/{id}/` | Einen Kurs aktualisieren |
| DELETE | `/courses/{id}/` | Einen Kurs löschen |

### 13.2 — App-URLs in der globalen `urls.py` registrieren

Bearbeiten Sie `djangoapi/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),  # '' = Wurzel — erreichbar unter localhost:8000/courses/
]
```

---

## 14. Die API testen

### Option A — Durchsuchbare API (in DRF eingebaut)

Rufen Sie **[http://localhost:8000/courses/](http://localhost:8000/courses/)** im Browser auf. DRF zeigt eine benutzerfreundliche Oberfläche an, über die Sie Daten lesen und senden können — ganz ohne zusätzliche Werkzeuge.

### Option B — Postman oder Insomnia

Laden Sie [Postman](https://www.postman.com/) oder [Insomnia](https://insomnia.rest/) herunter und senden Sie Anfragen manuell:

```
GET    http://localhost:8000/courses/
POST   http://localhost:8000/courses/        Body: {"name": "Python", "language": "Python", "price": "29.99"}
PUT    http://localhost:8000/courses/1/      Body: {"name": "Python Pro", "language": "Python", "price": "49.99"}
DELETE http://localhost:8000/courses/1/
```

### Option C — curl (Terminal)

```bash
# Alle Kurse auflisten
curl http://localhost:8000/courses/

# Einen Kurs erstellen
curl -X POST http://localhost:8000/courses/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Python Grundlagen", "language": "Python", "price": "19.99"}'
```

---

## 15. Projekt auf GitHub hochladen

### 15.1 — `.gitignore`-Datei erstellen

Erstellen Sie vor dem ersten Commit eine `.gitignore`-Datei im Stammverzeichnis, um Dateien auszuschließen, die nicht verfolgt werden sollen:

```
# Virtuelle Umgebung
my_venv/

# Python-Cache
__pycache__/
*.pyc
*.pyo

# Django
*.sqlite3
*.log

# VS Code
.vscode/
```

### 15.2 — Git initialisieren und ersten Commit erstellen

```bash
git init
git add .
git commit -m "Erster Commit: Django REST API CRUD für Kurse"
```

### 15.3 — Mit GitHub verbinden und hochladen

```bash
git remote add origin https://github.com/Dargai/simpledjangoapi.git
git branch -M main
git push -u origin main
```

> Nach dem ersten Push können Sie für zukünftige Commits einfach `git push` verwenden.

### 15.4 — Typischer Arbeitsablauf nach Änderungen

```bash
git add .
git commit -m "Beschreibung der vorgenommenen Änderungen"
git push
```

---

## 📁 Finale Projektstruktur

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

## 📌 Kurzübersicht der Befehle

| Aktion | macOS / Linux | Windows Git Bash |
|---|---|---|
| Venv aktivieren | `source my_venv/bin/activate` | `source my_venv/Scripts/activate` |
| Migrationen anwenden | `python manage.py migrate` | `winpty python manage.py migrate` |
| Migrationen erstellen | `python manage.py makemigrations` | `winpty python manage.py makemigrations` |
| Server starten | `python manage.py runserver` | `winpty python manage.py runserver` |
| Superuser erstellen | `python manage.py createsuperuser` | `winpty python manage.py createsuperuser` |
| Neue App erstellen | `python manage.py startapp appname` | `winpty python manage.py startapp appname` |

---

*Erstellt mit ❤️ mithilfe von Django & Django REST Framework*
