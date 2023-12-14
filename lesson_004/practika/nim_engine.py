"""Функции управления игрой"""
from random import randint

MAX_BUNCHES = 5

_holder = []


def put_stones():
    """Функция разложения камней"""
    global _holder
    _holder = []
    for i in range(5):
        _holder.append(randint(1, 20))


def take_from_brunch(position, quantity):
    """Взять из кучи"""
    if 1 <= position <= len(_holder):
        _holder[position - 1] -= quantity


def get_bunches():
    """Функция положения камней. Возвращает список [XX, YY, ZZ, ...] - текущее расположение камней"""
    return _holder


def is_gameover():
    """Конец игры. Возвращает True если больше ходов сделать нельзя"""
    return sum(_holder) == 0
