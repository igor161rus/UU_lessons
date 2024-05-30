from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Добро пожаловать на платформу для распознавания объектов.</h1>")


def dashboard(request):
    return HttpResponse("dashboard")
