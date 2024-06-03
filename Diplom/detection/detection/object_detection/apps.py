from django.apps import AppConfig


class ObjectDetectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'object_detection'
    verbose_name = 'Обнаружение объектов'


class ImageFeedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'image_feed'
    verbose_name = 'Изображения'
