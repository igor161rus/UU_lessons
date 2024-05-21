from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def get_courses_page(request):
    return HttpResponse("<ol> "
                        "<li>Курс 1</li>"
                        "<li>Курс 2</li>"
                        " </ol>")


def get_courses_news(request):
    return HttpResponse('Новости курсов')


courses_name = {
    1: 'python',
    2: 'rust',
    3: 'java'
}


def get_course_by_id(request, id: int):
    if id in courses_name:
        return HttpResponseRedirect(f'/courses/{courses_name[id]}/')
    else:
        return HttpResponse(f'Не существует курс номер: {id}')


def get_course_by_name(request, id):
    return HttpResponse(f'Это курс под названием: {id}')
