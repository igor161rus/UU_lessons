from django.urls import path, include
from .views import get_courses_page

urlpatterns = [
    path('', get_courses_page),
    # path('news/', get_courses_news),
    # path('id/', get_course)
    ]