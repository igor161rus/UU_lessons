from django.urls import path, include
from .views import get_courses_page, get_courses_news, get_course_by_id, get_course_by_name

urlpatterns = [
    path('', get_courses_page),
    path('news/', get_courses_news),
    path('<int:id>/', get_course_by_id),
    path('<str:id>/', get_course_by_name)
    ]
