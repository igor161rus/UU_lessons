from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def get_courses_page(request):
    return HttpResponse("<ol> "
                        "<li>Курс 1</li>"
                        "<li>Курс 2</li>"
                        " </ol>")
