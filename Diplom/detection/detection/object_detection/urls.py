from django.urls import path, include
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('about/', about, name='about'),
    path('image/<int:pk>/', image, name='image'),
    path('add-image-feed/', add_image_feed, name='add_image_feed'),
    path('process/<int:feed_id>/', process_image_feed, name='process_feed'),
    path('delete-image/<int:pk>/', delete_image, name='delete_image'),
    path('category/<int:cat_id>/', category, name='category'),
    path('image_detect/<int:pk>/', image_detect, name='image_detect'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
