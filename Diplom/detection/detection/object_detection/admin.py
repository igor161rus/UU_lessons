from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django_admin_geomap import ModelAdmin

from .models import *


class DetectedObjectAdmin(admin.ModelAdmin):
    list_display = ('image_feed', 'object_type', 'confidence', 'location', 'processed_image', 'method_detected')
    list_display_links = ('image_feed',)
    search_fields = ('object_type', 'location')


class ImageFeedAdmin(ModelAdmin):
    # list_display = ('user', 'image', 'processed_image')
    list_display = ('user', 'image', 'lon', 'lat')
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"


class UserInline(admin.StackedInline):
    model = UserAddFields
    can_delete = False
    verbose_name_plural = "Дополнительные поля"


class UserAdmin(BaseUserAdmin):
    inlines = [UserInline]


admin.site.unregister(User)
admin.site.register(ImageFeed, ImageFeedAdmin)
admin.site.register(DetectedObject, DetectedObjectAdmin)
admin.site.register(User, UserAdmin)
