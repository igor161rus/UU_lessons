from django import template
import datetime

register = template.Library()


# from django import template
# from object_detection.models import *
#
# register = template.Library()
#
#
# @register.simple_tag
# def get_image_feeds():
#     return ImageFeed.objects.all()

@register.simple_tag
def current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
