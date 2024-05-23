from django.shortcuts import render
from django.http import HttpResponse


def task_list(request, *args, **kwargs):
    # return HttpResponse('<ul>'
    #                     '<li>Task 1</li>'
    #                     '<li>Task 2</li>'
    #                     '<li>Task 3</li>'
    #                     '</ul>'
    #                     )
    return render(request, 'task_list.html', {})
