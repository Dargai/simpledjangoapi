# 📚 Simple Django REST API — Projet CRUD Cours

Une API REST accessible aux débutants, construite avec **Django** et **Django REST Framework (DRF)**.
Ce projet expose une interface CRUD complète pour un catalogue de cours en ligne, permettant de créer, lire, mettre à jour et supprimer des cours via les méthodes HTTP standard (GET, POST, PUT, DELETE).

> **Objectif de ce guide :** Comprendre ce qu'est Django REST Framework, comment il fonctionne, et suivre chaque étape — de la configuration de l'environnement jusqu'au déploiement sur GitHub.

---

## 🗂️ Table des matières

1. [Qu'est-ce que Django REST Framework ?](#1-quest-ce-que-django-rest-framework-)
2. [Prérequis & Outils](#2-prérequis--outils)
3. [Configuration de l'environnement](#3-configuration-de-lenvironnement)
4. [Installation de Django & DRF](#4-installation-de-django--drf)
5. [Création du projet Django](#5-création-du-projet-django)
6. [Création de l'application](#6-création-de-lapplication)
7. [Configuration de `settings.py`](#7-configuration-de-settingspy)
8. [Migrations & lancement du serveur](#8-migrations--lancement-du-serveur)
9. [Interface d'administration Django](#9-interface-dadministration-django)
10. [Création du modèle](#10-création-du-modèle)
11. [Création du sérialiseur](#11-création-du-sérialiseur)
12. [Création de la vue](#12-création-de-la-vue)
13. [Configuration des URLs & routes](#13-configuration-des-urls--routes)
14. [Tester l'API](#14-tester-lapi)
15. [Pousser le projet sur GitHub](#15-pousser-le-projet-sur-github)

---

## 1. Qu'est-ce que Django REST Framework ?

**Django** est un framework web Python de haut niveau qui favorise un développement rapide et une conception propre et pragmatique.

**Django REST Framework (DRF)** est une boîte à outils puissante construite par-dessus Django qui facilite la création d'APIs Web. Il fournit :

- **Les sérialiseurs (Serializers)** — convertissent les objets Python (modèles) en JSON et inversement
- **Les ViewSets** — des vues basées sur des classes qui gèrent automatiquement toutes les opérations CRUD
- **Les routeurs (Routers)** — câblent automatiquement les méthodes HTTP (GET, POST, PUT, DELETE) aux URLs
- **Une API navigable** — une interface web intégrée pour explorer et tester votre API directement dans le navigateur

Le flux typique d'une requête DRF ressemble à ceci :

```
Requête HTTP → Routeur URL → ViewSet → Sérialiseur → Modèle (Base de données)
                                                            ↕
Réponse HTTP ← Routeur URL ← ViewSet ← Sérialiseur ← Modèle (Base de données)
```

---

## 2. Prérequis & Outils

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

| Outil | Utilité | Téléchargement |
|---|---|---|
| **Python 3.10+** | Environnement d'exécution | [python.org](https://www.python.org/downloads/) |
| **pip** | Gestionnaire de paquets Python | Inclus avec Python |
| **VS Code** ou **Sublime Text** | Éditeur de code | [code.visualstudio.com](https://code.visualstudio.com/) |
| **Git Bash** (Windows) | Terminal | [git-scm.com](https://git-scm.com/) |
| **Git** | Contrôle de version | [git-scm.com](https://git-scm.com/) |

> 💡 **Utilisateurs Windows avec Git Bash :** Certaines commandes Python nécessitent le préfixe `winpty` pour fonctionner correctement dans Git Bash (ex. : `winpty python manage.py runserver`). Ce guide signalera chaque endroit où cela s'applique.

---

## 3. Configuration de l'environnement

### 3.1 — Créer le dossier du projet

```bash
mkdir djangoapi
cd djangoapi
```

### 3.2 — Créer un environnement virtuel

Un environnement virtuel isole les dépendances de votre projet du reste de votre système.

```bash
python -m venv my_venv
```

### 3.3 — Activer l'environnement virtuel

| Plateforme | Commande |
|---|---|
| **Windows (Git Bash)** | `source my_venv/Scripts/activate` |
| **macOS / Linux** | `source my_venv/bin/activate` |

Une fois activé, votre terminal affichera `(my_venv)` au début de la ligne — c'est la confirmation que l'environnement est actif.

### 3.4 — Vérifier l'environnement

```bash
pip freeze
```

Cette commande liste tous les paquets installés. Dans un environnement virtuel tout neuf, elle ne devrait rien retourner (ou presque).

### 3.5 — Désactiver l'environnement quand vous avez terminé

```bash
deactivate
```

---

## 4. Installation de Django & DRF

Assurez-vous que votre environnement virtuel est **actif** avant d'exécuter ces commandes.

```bash
pip install Django
pip install djangorestframework
```

Après l'installation, `pip freeze` devrait afficher quelque chose comme :

```
asgiref==3.11.1
Django==6.0.3
djangorestframework==3.16.1
sqlparse==0.5.5
tzdata==2025.3
```

> Les versions affichées peuvent être différentes — c'est tout à fait normal.

---

## 5. Création du projet Django

### 5.1 — Démarrer le projet

```bash
django-admin startproject djangoapi .
```

> Le `.` final crée le projet dans le dossier courant au lieu de créer un sous-dossier imbriqué. Cela garde une structure plus claire.

### 5.2 — Comprendre la structure générée

```
djangoapi/
├── manage.py          ← point d'entrée pour toutes les commandes Django
└── djangoapi/
    ├── __init__.py
    ├── settings.py    ← configuration du projet
    ├── urls.py        ← routage global des URLs
    ├── asgi.py
    └── wsgi.py
```

> ⚠️ **Exécutez toujours les commandes Django depuis le dossier qui contient `manage.py`.**

---

## 6. Création de l'application

Un **projet** Django peut contenir plusieurs **applications**. Chaque application gère une fonctionnalité spécifique. Ici, nous créons une application `courses`.

```bash
python manage.py startapp courses
```

Cela génère la structure suivante à l'intérieur de votre projet :

```
courses/
├── admin.py
├── apps.py
├── models.py       ← définissez vos modèles de données ici
├── serializers.py  ← vous allez créer ce fichier
├── urls.py         ← vous allez créer ce fichier
├── views.py
└── migrations/
```

---

## 7. Configuration de `settings.py`

Ouvrez `djangoapi/settings.py` et ajoutez `rest_framework` ainsi que votre nouvelle application dans `INSTALLED_APPS` :

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Librairies tierces
    'rest_framework',

    # Vos applications
    'courses',
]
```

---

## 8. Migrations & lancement du serveur

Django est livré avec une base de données intégrée (SQLite) et des modèles préconstruits (utilisateurs, admin, etc.). Vous devez les appliquer avant que quoi que ce soit ne fonctionne.

### 8.1 — Appliquer les migrations initiales

| Plateforme | Commande |
|---|---|
| **macOS / Linux** | `python manage.py migrate` |
| **Windows (Git Bash)** | `winpty python manage.py migrate` |

### 8.2 — Démarrer le serveur de développement

| Plateforme | Commande |
|---|---|
| **macOS / Linux** | `python manage.py runserver` |
| **Windows (Git Bash)** | `winpty python manage.py runserver` |

Ouvrez votre navigateur et allez sur **[http://localhost:8000](http://localhost:8000)**. Vous devriez voir la page d'accueil de Django. 🎉

---

## 9. Interface d'administration Django

Django fournit un panneau d'administration intégré accessible à `http://localhost:8000/admin/` où vous pouvez gérer vos enregistrements de base de données directement depuis le navigateur.

### 9.1 — Créer un superutilisateur (compte administrateur)

| Plateforme | Commande |
|---|---|
| **macOS / Linux** | `python manage.py createsuperuser` |
| **Windows (Git Bash)** | `winpty python manage.py createsuperuser` |

Suivez les instructions pour définir un nom d'utilisateur, un email et un mot de passe.

### 9.2 — Accéder au panneau d'administration

Redémarrez le serveur et allez sur `http://localhost:8000/admin/`, puis connectez-vous avec vos identifiants.

---

## 10. Création du modèle

Un **modèle** est une classe Python qui représente une table de base de données. Chaque attribut devient une colonne.

### 10.1 — Définir le modèle `Course`

Modifiez `courses/models.py` :

```python
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name  # Affiche le nom du cours au lieu de "Course object (1)" dans l'admin
```

### 10.2 — Créer et appliquer les migrations

Chaque fois que vous créez ou modifiez un modèle, vous devez exécuter deux commandes :

```bash
# Générer le fichier de migration
python manage.py makemigrations

# L'appliquer à la base de données
python manage.py migrate
```

> **Git Bash sur Windows :** ajoutez `winpty` devant les deux commandes.

### 10.3 — Enregistrer le modèle dans l'interface d'administration

Modifiez `courses/admin.py` :

```python
from django.contrib import admin
from .models import Course

admin.site.register(Course)
```

Vous pouvez maintenant ajouter, modifier et supprimer des cours directement depuis `http://localhost:8000/admin/`.

---

## 11. Création du sérialiseur

Un **sérialiseur** convertit un objet `Course` en JSON (pour l'envoyer au client) et convertit le JSON entrant en objet `Course` (pour le sauvegarder en base de données).

Créez un nouveau fichier `courses/serializers.py` :

```python
from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'url', 'name', 'language', 'price')
```

> `HyperlinkedModelSerializer` ajoute un champ `url` qui agit comme un lien cliquable vers chaque ressource cours — rendant l'API plus facile à naviguer.

---

## 12. Création de la vue

Un **ViewSet** regroupe toute la logique CRUD (lister, créer, récupérer, mettre à jour, supprimer) dans une seule classe. DRF gère le reste automatiquement.

Modifiez `courses/views.py` :

```python
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()       # Récupère tous les cours depuis la base de données
    serializer_class = CourseSerializer   # Utilise notre sérialiseur pour formater les données
```

---

## 13. Configuration des URLs & routes

### 13.1 — Créer `courses/urls.py`

L'application `courses` n'a pas de fichier `urls.py` par défaut — vous devez le créer :

```python
from django.urls import path, include
from rest_framework import routers
from . import views

# Un routeur crée automatiquement les URLs pour toutes les opérations CRUD
router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

Le routeur mappe automatiquement les routes suivantes :

| Méthode HTTP | URL | Action |
|---|---|---|
| GET | `/courses/` | Lister tous les cours |
| POST | `/courses/` | Créer un nouveau cours |
| GET | `/courses/{id}/` | Récupérer un cours |
| PUT | `/courses/{id}/` | Mettre à jour un cours |
| DELETE | `/courses/{id}/` | Supprimer un cours |

### 13.2 — Enregistrer les URLs de l'app dans le `urls.py` global

Modifiez `djangoapi/urls.py` :

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),  # '' = racine — accessible à localhost:8000/courses/
]
```

---

## 14. Tester l'API

### Option A — API navigable (intégrée à DRF)

Allez sur **[http://localhost:8000/courses/](http://localhost:8000/courses/)** dans votre navigateur. DRF affiche une interface conviviale où vous pouvez lire et envoyer des données sans aucun outil supplémentaire.

### Option B — Postman ou Insomnia

Téléchargez [Postman](https://www.postman.com/) ou [Insomnia](https://insomnia.rest/) et envoyez des requêtes manuellement :

```
GET    http://localhost:8000/courses/
POST   http://localhost:8000/courses/        Corps: {"name": "Python", "language": "Python", "price": "29.99"}
PUT    http://localhost:8000/courses/1/      Corps: {"name": "Python Pro", "language": "Python", "price": "49.99"}
DELETE http://localhost:8000/courses/1/
```

### Option C — curl (terminal)

```bash
# Lister tous les cours
curl http://localhost:8000/courses/

# Créer un cours
curl -X POST http://localhost:8000/courses/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Les bases de Python", "language": "Python", "price": "19.99"}'
```

---

## 15. Pousser le projet sur GitHub

### 15.1 — Créer un fichier `.gitignore`

Avant de faire un commit, créez un fichier `.gitignore` à la racine de votre projet pour exclure les fichiers qui ne doivent pas être suivis :

```
# Environnement virtuel
my_venv/

# Cache Python
__pycache__/
*.pyc
*.pyo

# Django
*.sqlite3
*.log

# VS Code
.vscode/
```

### 15.2 — Initialiser Git et faire le premier commit

```bash
git init
git add .
git commit -m "Premier commit : API REST Django CRUD pour les cours"
```

### 15.3 — Connecter à GitHub et pousser

```bash
git remote add origin https://github.com/Dargai/simpledjangoapi.git
git branch -M main
git push -u origin main
```

> Après le premier push, vous pouvez simplement utiliser `git push` pour les commits suivants.

### 15.4 — Flux de travail habituel après des modifications

```bash
git add .
git commit -m "décrivez ce que vous avez modifié"
git push
```

---

## 📁 Structure finale du projet

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

## 📌 Référence rapide des commandes

| Action | macOS / Linux | Windows Git Bash |
|---|---|---|
| Activer le venv | `source my_venv/bin/activate` | `source my_venv/Scripts/activate` |
| Appliquer les migrations | `python manage.py migrate` | `winpty python manage.py migrate` |
| Créer les migrations | `python manage.py makemigrations` | `winpty python manage.py makemigrations` |
| Lancer le serveur | `python manage.py runserver` | `winpty python manage.py runserver` |
| Créer un superutilisateur | `python manage.py createsuperuser` | `winpty python manage.py createsuperuser` |
| Créer une nouvelle app | `python manage.py startapp nomapp` | `winpty python manage.py startapp nomapp` |

---

*Fait avec ❤️ en utilisant Django & Django REST Framework*
