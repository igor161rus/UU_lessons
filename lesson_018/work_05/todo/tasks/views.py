from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView


def task_list(request, *args, **kwargs):
    tasks = ['Task 1', 'Task 2', 'Task 3']
    # return HttpResponse('<ul>'
    #                     '<li>Task 1</li>'
    #                     '<li>Task 2</li>'
    #                     '<li>Task 3</li>'
    #                     '</ul>'
    #                     )
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


class AboutView(TemplateView):
    template_name = 'tasks/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Tasks'
        context['title'] = 'About'
        context['description'] = 'About Tasks. It is a simple todo app.'
        return context
