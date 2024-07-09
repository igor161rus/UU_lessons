from django import template

from ..models import *

register = template.Library()


@register.simple_tag
def get_likes_count():
    user_id = 5
    count = Advertisement.objects.filter(user_id=user_id).count()
    print(111111, count)
    return count
