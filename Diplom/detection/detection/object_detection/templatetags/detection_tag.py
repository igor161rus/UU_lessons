from django import template
# import datetime
from ..models import *
from django.db.models import Count

register = template.Library()


@register.simple_tag
def current_stat(id):
    stat = DetectedObject.objects.filter(image_feed=id).values('object_type', 'method_detected').annotate(Count('object_type'))
    return stat
