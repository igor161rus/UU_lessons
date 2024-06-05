from django import template
from object_detection.models import *

register = template.Library()


@register.simple_tag
def get_image_feeds():
    return ImageFeed.objects.all()