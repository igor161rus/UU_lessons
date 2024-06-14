from django import template
# import datetime
from ..models import *
from django.db.models import Count

register = template.Library()


@register.simple_tag
def current_stat(id):
    stat = DetectedObject.objects.filter(image_feed=id).values('object_type', 'method_detected').annotate(
        Count('object_type'))
    return stat


@register.simple_tag
def get_all_type():
    type_detected = DetectedObject.objects.order_by('object_type').values('object_type', 'image_feed_id').distinct()
    return type_detected


@register.inclusion_tag('object_detection/list_category.html')
def show_categories(cat_selected=0):
    type_detected = DetectedObject.objects.order_by('object_type').values('object_type', 'image_feed_id').distinct()
    cats = type_detected.imap(lambda x: (x['object_type'], x['image_feed_id']))
    return {'type_detected': type_detected.object_type, 'cats': cats, 'cat_selected': cat_selected}
