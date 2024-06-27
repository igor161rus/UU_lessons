from django import template
# import datetime
from ..models import *
from django.db.models import Count
from django_admin_geomap import geomap_context

register = template.Library()


@register.simple_tag
def current_stat(id):
    """
        Возвращает количество обнаруженных объектов, сгруппированных по типу объекта и методу обнаружения
        для определенного изображения.
        Args:
            id (int): идентификатор изображения, для которого требуется получить статистику обнаружения.
        Returns:
            QuerySet: набор, содержащий количество обнаруженных объектов, сгруппированных по типу объекта
             и методу обнаружения.
    """
    stat = DetectedObject.objects.filter(image_feed=id).values('object_type', 'method_detected').annotate(
        Count('object_type'))
    return stat


@register.simple_tag
def get_all_type():
    """
        Получает список уникальных типов объектов вместе со связанными с ними идентификаторами изображений.
        Returns:
        list: список словарей, содержащих «object_type» и «image_feed_id».
    """
    type_detected = DetectedObject.objects.order_by('object_type').values('object_type', 'image_feed_id').distinct()
    return type_detected


@register.inclusion_tag('object_detection/list_categories.html')
def show_categories(cat_selected=0):
    """
        Функция получает список уникальных обнаруженных типов объектов вместе с соответствующими идентификаторами
            изображений и отображает их в шаблоне list_categories.html.
        Parameters:
        - cat_selected: целое число, представляющее выбранную категорию (по умолчанию — 0).
        Returns:
        Словарь, содержащий извлеченные обнаруженные типы объектов и идентификаторы изображений,
            а также выбранную категорию.
    """
    type_detected = DetectedObject.objects.order_by('object_type').values('object_type', 'image_feed_id').distinct()
    t_list = []
    for t in type_detected:
        t_list.append(t['object_type'])
    return {'type_detected': type_detected,  'cat_selected': cat_selected}


@register.inclusion_tag('geomap/common.html')
def get_map(user_id):
    """
        Выводит карту с геометками
        Returns:
        list: список словарей, содержащих «object_type» и «image_feed_id».
    """
    return geomap_context(ImageFeed.objects.filter(user=user_id))
