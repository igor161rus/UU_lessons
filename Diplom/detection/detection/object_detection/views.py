from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import *

menu = ['Главная', 'О сайте', 'приборная доска']


def home(request):
    posts = ImageFeed.objects.all()
    return render(request, "object_detection/home.html", {'posts': posts, 'menu': menu, 'title': 'Главная'})


def about(request):
    return render(request, "object_detection/about.html", {"title": "О сайте"})


def dashboard(request):
    return HttpResponse("dashboard")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
