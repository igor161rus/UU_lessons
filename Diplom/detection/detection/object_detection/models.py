from django.db import models
from django.conf import settings


class ImageFeed(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    processed_image = models.ImageField(upload_to='processed_images/', null=True, blank=True, verbose_name='Обработанное изображение')

    def __str__(self):
        return f"{self.user.username} - {self.image.name}"

    def get_absolute_url(self):
        return f"/{self.pk}/"

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['-pk']


class DetectedObject(models.Model):
    image_feed = models.ForeignKey(ImageFeed, related_name='detected_objects', on_delete=models.CASCADE)
    object_type = models.CharField(max_length=100)
    confidence = models.FloatField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.object_type} ({self.confidence * 100}%) on {self.image_feed.image.name}"

    def get_absolute_url(self):
        return f"/{self.pk}/"

    class Meta:
        verbose_name = 'Обнаруженный объект'
        verbose_name_plural = 'Обнаруженные объекты'
        ordering = ['-pk']
