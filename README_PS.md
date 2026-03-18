<div dir="rtl">

# 📚 ساده Django REST API — د کورسونو CRUD پروژه

یوه پیل کوونکو ته مناسبه REST API، چې د **Django** او **Django REST Framework (DRF)** سره جوړه شوې ده.
دا پروژه د آنلاین کورسونو د کټالوګ لپاره یوه بشپړه CRUD انٹرفیس وړاندې کوي، چې تاسو ته اجازه درکوي د معیاري HTTP میتوډونو (GET, POST, PUT, DELETE) له لارې کورسونه جوړ کړئ، ولولئ، تازه کړئ او ړنګ کړئ.

> **د دې لارښود موخه:** پوه شئ چې Django REST Framework څه شی دی، څنګه کار کوي، او هر ګام تعقیب کړئ — د چاپیریال د جوړولو نه تر GitHub پورې.

---

## 🗂️ د موادو فهرست

1. [Django REST Framework څه شی دی؟](#1-django-rest-framework-څه-شی-دی)
2. [مخکینۍ اړتیاوې او وسیلې](#2-مخکینۍ-اړتیاوې-او-وسیلې)
3. [چاپیریال تنظیمول](#3-چاپیریال-تنظیمول)
4. [Django او DRF نصبول](#4-django-او-drf-نصبول)
5. [د Django پروژه جوړول](#5-د-django-پروژه-جوړول)
6. [اپلیکیشن جوړول](#6-اپلیکیشن-جوړول)
7. [`settings.py` تنظیمول](#7-settingspy-تنظیمول)
8. [مایګریشنونه او سرور پیلول](#8-مایګریشنونه-او-سرور-پیلول)
9. [د Django ادمین سیمه](#9-د-django-ادمین-سیمه)
10. [ماډل جوړول](#10-ماډل-جوړول)
11. [سریالایزر جوړول](#11-سریالایزر-جوړول)
12. [ویو جوړول](#12-ویو-جوړول)
13. [د URLs او روټونو تنظیمول](#13-د-urls-او-روټونو-تنظیمول)
14. [د API ازموینه](#14-د-api-ازموینه)
15. [پروژه GitHub ته وړل](#15-پروژه-github-ته-وړل)

---

## 1. Django REST Framework څه شی دی؟

**Django** یو لوړ کچې Python ویب فریمورک دی چې ګړندۍ پرمختیا او سمه، عملي ډیزاین هڅوي.

**Django REST Framework (DRF)** یو پیاوړی ټولګه دی چې د Django سر ته جوړ شوی او د ویب APIs جوړول ډیر اسانه کوي. دا لاندې شیان وړاندې کوي:

- **Serializers** — د Python آبجکتونه (ماډلونه) JSON ته او بیرته بدلوي
- **ViewSets** — د کلاس پر بنسټ ویوونه چې ټول CRUD عملیات اتوماتیک اداره کوي
- **Routers** — HTTP میتوډونه (GET, POST, PUT, DELETE) اتوماتیک د URLs سره وصلوي
- **د لیدلو وړ API** — یوه جوړه شوې ویب انٹرفیس چې تاسو کولای شئ خپله API مستقیم له براوزر نه وڅیړئ

د DRF د غوښتنې عمومي جریان داسې دی:

```
HTTP غوښتنه → URL Router → ViewSet → Serializer → ماډل (ډیټابیس)
                                                          ↕
HTTP ځواب ← URL Router ← ViewSet ← Serializer ← ماډل (ډیټابیس)
```

---

## 2. مخکینۍ اړتیاوې او وسیلې

د پیلولو دمخه، ډاډ ترلاسه کړئ چې لاندې برنامې ستاسو کمپیوټر کې نصب دي:

| وسیله | موخه | ډاونلوډ |
|---|---|---|
| **Python 3.10+** | د چلولو چاپیریال | [python.org](https://www.python.org/downloads/) |
| **pip** | د Python د کڅوړو مدیریت | د Python سره راځي |
| **VS Code** یا **Sublime Text** | د کوډ سمونکی | [code.visualstudio.com](https://code.visualstudio.com/) |
| **Git Bash** (Windows) | ټرمینل | [git-scm.com](https://git-scm.com/) |
| **Git** | د نسخو کنټرول | [git-scm.com](https://git-scm.com/) |

> 💡 **د Windows کاروونکي چې Git Bash کاروي:** ځینې Python کمانډونه د `winpty` مخوندې ته اړتیا لري چې د Git Bash کې سمه کار وکړي (د بیلګې په توګه: `winpty python manage.py runserver`). دا لارښود به هر ځای چې دا اړتیا وي ښکاره کړي.

---

## 3. چاپیریال تنظیمول

### 3.1 — د پروژې فولډر جوړول

```bash
mkdir djangoapi
cd djangoapi
```

### 3.2 — مجازي چاپیریال جوړول

مجازي چاپیریال ستاسو د پروژې انحصارونه د سیستم له نورو برخو جلا ساتي.

```bash
python -m venv my_venv
```

### 3.3 — مجازي چاپیریال فعالول

| پلیټفارم | کمانډ |
|---|---|
| **Windows (Git Bash)** | `source my_venv/Scripts/activate` |
| **macOS / Linux** | `source my_venv/bin/activate` |

د فعالولو وروسته، ستاسو ټرمینل به د کرښې په پیل کې `(my_venv)` وښایي — دا تایيدوي چې چاپیریال فعال دی.

### 3.4 — چاپیریال تایید کول

```bash
pip freeze
```

دا کمانډ ټول نصب شوي کڅوړې لیست کوي. یوه تازه مجازي چاپیریال کې، باید هیڅ شی (یا ډیر لږ) نه ښکاره شي.

### 3.5 — د کار پای ته رسیدو وروسته چاپیریال غیرفعالول

```bash
deactivate
```

---

## 4. Django او DRF نصبول

دا کمانډونه چلولو دمخه، ډاډ ترلاسه کړئ چې ستاسو مجازي چاپیریال **فعال** دی.

```bash
pip install Django
pip install djangorestframework
```

د نصبولو وروسته، `pip freeze` باید داسې یو شی وښایي:

```
asgiref==3.11.1
Django==6.0.3
djangorestframework==3.16.1
sqlparse==0.5.5
tzdata==2025.3
```

> ستاسو ښودل شوي نسخې کیدای شي توپیر ولري — دا بالکل نورمال دي.

---

## 5. د Django پروژه جوړول

### 5.1 — پروژه پیلول

```bash
django-admin startproject djangoapi .
```

> د پای `.` پروژه اوسني فولډر کې جوړوي د ځانګړي فرعي فولډر د جوړولو پر ځای. دا جوړښت ساده ساتي.

### 5.2 — د جوړ شوي جوړښت پوهیدل

```
djangoapi/
├── manage.py          ← د ټولو Django کمانډونو لپاره د ننوتلو نقطه
└── djangoapi/
    ├── __init__.py
    ├── settings.py    ← د پروژې تنظیمات
    ├── urls.py        ← نړیوال URL روټینګ
    ├── asgi.py
    └── wsgi.py
```

> ⚠️ **تل د Django کمانډونه هغه فولډر نه چلوئ چې `manage.py` پکې وي.**

---

## 6. اپلیکیشن جوړول

یوه Django **پروژه** کیدای شي ډیرې **اپلیکیشنونه** ولري. هره اپلیکیشن یوه ځانګړې فیچر اداره کوي. دلته موږ یوه `courses` اپلیکیشن جوړوو.

```bash
python manage.py startapp courses
```

دا ستاسو د پروژې دننه لاندې جوړښت رامنځته کوي:

```
courses/
├── admin.py
├── apps.py
├── models.py       ← دلته خپل ډیټا ماډلونه تعریف کړئ
├── serializers.py  ← تاسو به دا فایل پخپله جوړ کړئ
├── urls.py         ← تاسو به دا فایل پخپله جوړ کړئ
├── views.py
└── migrations/
```

---

## 7. `settings.py` تنظیمول

`djangoapi/settings.py` خلاص کړئ او `rest_framework` او خپله نوې اپلیکیشن `INSTALLED_APPS` ته اضافه کړئ:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # د دریمې خوا کتابتونونه
    'rest_framework',

    # ستاسو اپلیکیشنونه
    'courses',
]
```

---

## 8. مایګریشنونه او سرور پیلول

Django د جوړ شوي ډیټابیس (SQLite) او ځینو مخکیني ماډلونو (کاروونکي، ادمین، او نور) سره راځي. دا باید د هر شي د کار کولو دمخه تطبیق شي.

### 8.1 — لومړني مایګریشنونه تطبیق کول

| پلیټفارم | کمانډ |
|---|---|
| **macOS / Linux** | `python manage.py migrate` |
| **Windows (Git Bash)** | `winpty python manage.py migrate` |

### 8.2 — د پرمختیا سرور پیلول

| پلیټفارم | کمانډ |
|---|---|
| **macOS / Linux** | `python manage.py runserver` |
| **Windows (Git Bash)** | `winpty python manage.py runserver` |

خپل براوزر خلاص کړئ او **[http://localhost:8000](http://localhost:8000)** ته لاړ شئ. تاسو باید د Django د ښه راغلاست پاڼه وګورئ. 🎉

---

## 9. د Django ادمین سیمه

Django د `http://localhost:8000/admin/` پته کې یوه جوړه شوې ادمین پینل وړاندې کوي چیرې چې تاسو کولای شئ مستقیم له براوزر نه د ډیټابیس ریکارډونه اداره کړئ.

### 9.1 — سوپر کاروونکی (د ادمین حساب) جوړول

| پلیټفارم | کمانډ |
|---|---|
| **macOS / Linux** | `python manage.py createsuperuser` |
| **Windows (Git Bash)** | `winpty python manage.py createsuperuser` |

د کاروونکي نوم، بریښنالیک او پاسورډ ټاکلو لپاره لارښوونې تعقیب کړئ.

### 9.2 — ادمین پینل ته لاسرسی

سرور بیا پیل کړئ او `http://localhost:8000/admin/` ته لاړ شئ، بیا د خپلو معلوماتو سره ننوځئ.

---

## 10. ماډل جوړول

یو **ماډل** یوه Python کلاس ده چې د ډیټابیس جدول استازیتوب کوي. هر صفت یوه کالم کیږي.

### 10.1 — د `Course` ماډل تعریف کول

`courses/models.py` سمون کړئ:

```python
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name  # د ادمین کې د "Course object (1)" پر ځای د کورس نوم ښایي
```

### 10.2 — مایګریشنونه جوړول او تطبیق کول

هر ځل چې تاسو ماډل جوړ کړئ یا سمون کړئ، باید دوه کمانډونه چلوئ:

```bash
# د مایګریشن فایل رامنځته کول
python manage.py makemigrations

# ډیټابیس ته یې تطبیق کول
python manage.py migrate
```

> **د Windows کاروونکي Git Bash کې:** دواړه کمانډونو ته `winpty` اضافه کړئ.

### 10.3 — ماډل د ادمین سیمې کې ثبتول

`courses/admin.py` سمون کړئ:

```python
from django.contrib import admin
from .models import Course

admin.site.register(Course)
```

اوس تاسو کولای شئ مستقیم د `http://localhost:8000/admin/` له لارې کورسونه اضافه، سمون او ړنګ کړئ.

---

## 11. سریالایزر جوړول

یو **Serializer** یو `Course` آبجکت JSON ته بدلوي (د پیرودونکي ته د لیږلو لپاره) او راتلونکی JSON بیرته `Course` آبجکت ته بدلوي (د ډیټابیس کې د ذخیره کولو لپاره).

یوه نوې فایل `courses/serializers.py` جوړه کړئ:

```python
from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'url', 'name', 'language', 'price')
```

> `HyperlinkedModelSerializer` یو `url` فیلډ اضافه کوي چې د هر کورس سرچینې ته د کلیک وړ لینک کار کوي — چې API ناویګیشن اسانه کوي.

---

## 12. ویو جوړول

یو **ViewSet** ټول CRUD منطق (لیست کول، جوړول، ترلاسه کول، تازه کول، ړنګول) یوې کلاس کې یوځای کوي. DRF پاتې کارونه اتوماتیک اداره کوي.

`courses/views.py` سمون کړئ:

```python
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()       # له ډیټابیس نه ټول کورسونه ترلاسه کول
    serializer_class = CourseSerializer   # د ډیټا د فارمیټ کولو لپاره زموږ serializer کارول
```

---

## 13. د URLs او روټونو تنظیمول

### 13.1 — `courses/urls.py` جوړول

د `courses` اپلیکیشن د ډیفالټ `urls.py` نه لري — تاسو باید یې پخپله جوړ کړئ:

```python
from django.urls import path, include
from rest_framework import routers
from . import views

# یو روټر اتوماتیک د ټولو CRUD عملیاتو لپاره URLs جوړوي
router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

روټر اتوماتیک لاندې روټونه تنظیموي:

| HTTP میتوډ | URL | عمل |
|---|---|---|
| GET | `/courses/` | ټول کورسونه لیست کول |
| POST | `/courses/` | نوی کورس جوړول |
| GET | `/courses/{id}/` | یو کورس ترلاسه کول |
| PUT | `/courses/{id}/` | کورس تازه کول |
| DELETE | `/courses/{id}/` | کورس ړنګول |

### 13.2 — د اپلیکیشن URLs د نړیوال `urls.py` کې ثبتول

`djangoapi/urls.py` سمون کړئ:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),  # '' = ریښه — د localhost:8000/courses/ نه لاسرسی
]
```

---

## 14. د API ازموینه

### اختیار A — د لیدلو وړ API (DRF کې جوړ شوی)

**[http://localhost:8000/courses/](http://localhost:8000/courses/)** براوزر کې خلاص کړئ. DRF یوه کاروونکو پلوه انٹرفیس ښایي چیرې چې تاسو کولای شئ د هیڅ اضافي وسیلو پرته ډیټا ولولئ او ولیږئ.

### اختیار B — Postman یا Insomnia

[Postman](https://www.postman.com/) یا [Insomnia](https://insomnia.rest/) ډاونلوډ کړئ او لاسي غوښتنې ولیږئ:

```
GET    http://localhost:8000/courses/
POST   http://localhost:8000/courses/        Body: {"name": "Python", "language": "Python", "price": "29.99"}
PUT    http://localhost:8000/courses/1/      Body: {"name": "Python Pro", "language": "Python", "price": "49.99"}
DELETE http://localhost:8000/courses/1/
```

### اختیار C — curl (ټرمینل)

```bash
# ټول کورسونه لیست کول
curl http://localhost:8000/courses/

# یو کورس جوړول
curl -X POST http://localhost:8000/courses/ \
  -H "Content-Type: application/json" \
  -d '{"name": "د Python اساسات", "language": "Python", "price": "19.99"}'
```

---

## 15. پروژه GitHub ته وړل

### 15.1 — د `.gitignore` فایل جوړول

د لومړي commit دمخه، خپل د پروژې ریښه فولډر کې د `.gitignore` فایل جوړ کړئ ترڅو هغه فایلونه وشاړئ چې باید تعقیب نشي:

```
# مجازي چاپیریال
my_venv/

# د Python کیچ
__pycache__/
*.pyc
*.pyo

# Django
*.sqlite3
*.log

# VS Code
.vscode/
```

### 15.2 — Git پیلول او لومړی commit جوړول

```bash
git init
git add .
git commit -m "لومړی commit: د کورسونو لپاره Django REST API CRUD"
```

### 15.3 — GitHub سره وصلیدل او پورته کول

```bash
git remote add origin https://github.com/Dargai/simpledjangoapi.git
git branch -M main
git push -u origin main
```

> د لومړي push وروسته، د راتلونکو commits لپاره کولای شئ یوازې `git push` وکاروئ.

### 15.4 — د بدلونونو وروسته عمومي کاري جریان

```bash
git add .
git commit -m "د بدلونونو توضیح"
git push
```

---

## 📁 د پروژې وروستی جوړښت

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

## 📌 د کمانډونو لنډ لارښود

| عمل | macOS / Linux | Windows Git Bash |
|---|---|---|
| مجازي چاپیریال فعالول | `source my_venv/bin/activate` | `source my_venv/Scripts/activate` |
| مایګریشنونه تطبیق کول | `python manage.py migrate` | `winpty python manage.py migrate` |
| مایګریشنونه جوړول | `python manage.py makemigrations` | `winpty python manage.py makemigrations` |
| سرور پیلول | `python manage.py runserver` | `winpty python manage.py runserver` |
| سوپر کاروونکی جوړول | `python manage.py createsuperuser` | `winpty python manage.py createsuperuser` |
| نوې اپلیکیشن جوړول | `python manage.py startapp appname` | `winpty python manage.py startapp appname` |

---

*د ❤️ سره د Django او Django REST Framework له کارولو سره جوړ شوی*

</div>
