from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('dashboard/', dashboard),
    path('about/', about, name='about'),
]
