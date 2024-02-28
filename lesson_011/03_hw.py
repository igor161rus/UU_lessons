# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы,
# модуль, и другие свойства.
#
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#    - Тип объекта.
#    - Атрибуты объекта.
#    - Методы объекта.
#    - Модуль, к которому объект принадлежит.
#    - Другие интересные свойства объекта, учитывая его тип (по желанию).
#
#
# Пример работы:
# number_info = introspection_info(42)
# print(number_info)
#
# Вывод на консоль:
# {'type': 'int', 'attributes': ['__abs__', '__add__', ...], 'methods': [], 'module': '__main__'}
#
# Рекомендуется создавать свой класс и объект для лучшего понимания
import inspect
from inspect import signature


class MyClass:
    """Мой класс"""

    # hghjgjhghjg
    def __init__(self):
        self.attr = 10
        # jhgjhgjhg

    def method(self, value):
        """Что-то считает и печатает"""
        self.attr = self.attr + value
        print(self.attr)


def my_func(value):
    """Моя функция"""
    print(value * 10)


def my_func_gen():
    for value in range(5):
        yield value


def introspection_info(obj, g=globals()):
    dict_obj = {
        "<class 'function'>": 'function',
        "<class 'int'>": 'int',
        "<class 'str'": 'str',
        "<class 'generator'>": 'generator',
        "<class '__main__.": 'class'
    }
    dict_func = {
        'function': 'getfullargspec(',
        'generator': 'getgeneratorstate'
    }
    name_object = [n for n in g if id(g[n]) == id(obj)][0]
    print(f'Исследуем объект: {obj} имя {name_object}')
    print(type(obj))
    for i in str(obj):
        if i in str(type(obj)):
            print('Тип: ', dict_obj[i])
            # print(eval('inspect.' + dict_func[dict_obj[i]] + 'obj)'))
    # if inspect.isclass(obj):
    # for n in g:
    #     print(n)
    #     if inspect.isclass(obj) and hasattr(obj, '__class__') and hasattr(obj, '__name__'):
    #         name_object = [n for n in g if id(g[n]) == id(obj)][0]
    #         print(f'Тип: класс {name_object}')

    if callable(obj):
        print(f'Объект {obj.__name__} является вызываемым')
        sig = signature(obj)
        print(f'Принимает параметры: {sig}')
    # else:
    # print(f'Объект {obj.__name__} является невызываемым')
    # print(f'Объект {obj.__doc__} является вызываемым', callable(obj))
    print(inspect.getmembers('__main__'))
    print('*' * 20, '\n')


my_obj = MyClass()
my_int = 20
my_str = 'jhgjhg gjhg'
gen1 = my_func_gen()

introspection_info(MyClass)
introspection_info(my_func)
introspection_info(my_obj)
introspection_info(my_int)

introspection_info(gen1)

