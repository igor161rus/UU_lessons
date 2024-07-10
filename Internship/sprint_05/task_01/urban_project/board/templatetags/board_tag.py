from django import template
from ..models import *

register = template.Library()


@register.simple_tag
def get_likes_count(user_id):
    count_like = 0
    all_adv = Advertisement.objects.filter(author_id=user_id)
    for adv in all_adv:
        # print(adv.author_id, adv.id, adv.likes.all())
        if adv.likes.all():
            count_like += 1
    # print('count_like', count_like)
    # count_likes = Advertisement.objects.filter(likes__id=user_id).count() + 1
    # print('count_likes', count_likes)

    return count_like
