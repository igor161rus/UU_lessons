from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from django_admin_geomap import GeoItem


class ImageFeed(models.Model, GeoItem):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    lon = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        # return f"{self.user.username} - {self.image.name} - {self.lon} - {self.lat}"
        return self.image.name

    def get_absolute_url(self):
        # return f"/{self.pk}/"
        return reverse('image', kwargs={'pk': self.pk})

    @property
    def geomap_longitude(self):
        return '' if self.lon is None else str(self.lon)

    @property
    def geomap_latitude(self):
        return '' if self.lat is None else str(self.lat)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['-pk']


class DetectedObject(models.Model):
    image_feed = models.ForeignKey(ImageFeed, related_name='detected_objects', on_delete=models.CASCADE)
    object_type = models.CharField(max_length=100)
    confidence = models.FloatField()
    location = models.CharField(max_length=255)
    processed_image = models.ImageField(upload_to='processed_images/', null=True, blank=True,
                                        verbose_name='Обработанное изображение')
    method_detected = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.object_type} ({self.confidence * 100}%) on {self.image_feed.image.name} - {self.processed_image}"

    def get_absolute_url(self):
        return f"/{self.pk}/"
        # return reverse('image', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Обнаруженный объект'
        verbose_name_plural = 'Обнаруженные объекты'
        ordering = ['-pk']


class UserAddFields(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tg_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.tg_id}"

    class Meta:
        verbose_name = 'Дополнительные поля'
        verbose_name_plural = 'Дополнительные поля'
