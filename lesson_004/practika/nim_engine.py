"""Функции управления игрой"""
from random import randint

MAX_BUNCHES = 5
MAX_BUNCHES_SIZE = 20

_holder = {}


def put_stones():
    """Функция разложения камней"""
    global _holder
    _holder = {}
    for i in range(1, MAX_BUNCHES + 1):
        _holder[i] = (randint(1, 20))


def take_from_brunch(position, quantity):
    """Взять из кучи"""
    if position in _holder:
        _holder[position] -= quantity
        return True
    else:
        return False


def get_bunches():
    """Функция положения камней. Возвращает список [XX, YY, ZZ, ...] - текущее расположение камней"""
    res = []
    for key in sorted(_holder.keys()):
        res.append(_holder[key])
    return res


def is_gameover():
    """Конец игры. Возвращает True если больше ходов сделать нельзя"""
    return sum(_holder.values()) == 0
