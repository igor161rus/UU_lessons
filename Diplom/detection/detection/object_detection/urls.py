from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('about/', about, name='about'),
    path('image/<int:pk>/', image, name='image'),
]
