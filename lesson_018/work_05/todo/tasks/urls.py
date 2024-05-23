from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('about/', views.AboutView.as_view(), name='about'),
]