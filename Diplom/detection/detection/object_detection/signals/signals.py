from django.db.models.signals import pre_delete
from django.dispatch import receiver

from Diplom.detection.detection.object_detection.models import DetectedObject


@receiver(pre_delete, sender=DetectedObject)
def image_model_delete(sender, instance, **kwargs):
    if instance.image.name:
        instance.image.delete(False)
