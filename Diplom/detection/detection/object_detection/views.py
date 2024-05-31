from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def home(request):
    return render(request, "object_detection/home.html")


def dashboard(request):
    return HttpResponse("dashboard")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
