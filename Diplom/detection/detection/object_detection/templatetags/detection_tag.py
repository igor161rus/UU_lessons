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


@register.inclusion_tag('object_detection/list_categories.html')
def show_categories(cat_selected=0):
    type_detected = DetectedObject.objects.order_by('object_type').values('object_type', 'image_feed_id').distinct()
    t_list = []
    for t in type_detected:
        t_list.append(t['object_type'])
    return {'type_detected': type_detected,  'cat_selected': cat_selected}
