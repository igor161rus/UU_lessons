from django.contrib import admin

from .models import *


class DetectedObjectAdmin(admin.ModelAdmin):
    list_display = ('image_feed', 'object_type', 'confidence', 'location')
    list_display_links = ('image_feed',)
    search_fields = ('object_type', 'location')


class ImageFeedAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'processed_image')
    list_display_links = ('user', 'image')
    search_fields = ('user', 'image')


admin.site.register(ImageFeed, ImageFeedAdmin)
admin.site.register(DetectedObject, DetectedObjectAdmin)
