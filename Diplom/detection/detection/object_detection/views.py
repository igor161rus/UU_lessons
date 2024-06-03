from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = [
    {"title": "Главная", "url_name": "home"},
    {"title": "Приборная доска", "url_name": "dashboard"},
    {"title": "Войти", "url_name": "login"},
]


def home(request):
    posts = ImageFeed.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная'
    }
    return render(request, "object_detection/home.html", context=context)


def about(request):
    return render(request, "object_detection/about.html", {"title": "О сайте"})


def dashboard(request):
    return HttpResponse("dashboard")


def login(request):
    return HttpResponse("login")


def image(request, pk):
    try:
        image = ImageFeed.objects.get(pk=pk)
        return render(request, "object_detection/image.html", {"image": image})
    except:
        raise Http404


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
