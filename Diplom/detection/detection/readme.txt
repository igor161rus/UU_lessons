SQLLiteStudio
Bootstrap: https://getbootstrap.com

django-admin startproject detection
python manage.py runserver
python manage.py startapp object_detection
python manage.py makemigrations
python manage.py migrate
python manage.py sqlmigrate object_detection 0001

python manage.py migrate

# ORM
python manage.py shell
from object_detection.models import ImageFeed
ImageFeed(user='Igor')
w1 = _
w1
w1.save()
w1
w1.id
w1.user
w1.pk

from django.db import connection
connection.queries

w2 = ImageFeed(user='Maks')
w2.save()
connection.queries

w3 = ImageFeed()
w3.user = 'User3'
w3.save()

# object
ImageFeed.objects
w4 = ImageFeed.objects.create(user='User4')
w4
w4.user
w4.pk

ImageFeed.objects.all()
q = _
q[0]
q1[0].user
len(q)
for qi in q:
    print(qi.user)

ImageFeed.objects.filter(user='Igor')
# from django.db import connection
connection.queries

ImageFeed.objects.filter(pk=1)
ImageFeed.objects.filter(pk__gte=1)

ImageFeed.objects.exclude(pk=2)

ImageFeed.objects.get(pk=2) #должна быть только одна запись

ImageFeed.objects.filter(pk__lte=4.order_by('user')

ImageFeed.objects.order_by('user')
ImageFeed.objects.order_by('-user')

wu = ImageFeed.objects.get(pk=2)
wu.user = 'Igor_1'
wu.save()
connection.queries

wd = ImageFeed.objects.filter(pk__gte=2)
wd
wd.delete()

Шаблонизатор Jinja2:
https://www.youtube.com/watch?v=cFJqMXxVNsI&list=PLA0M1Bcd0w8wfmtElObQrBbZjY6XeA06U&index=1&t=0s