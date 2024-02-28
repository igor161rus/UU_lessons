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
    def __init__(self, a):
        self.attr = 10
        self.a = a
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


def get_all_methods_details(obj):
    return [method for method in dir(obj) if method.startswith('__') is False]


def introspection_info(obj, g=globals()):
    dict_obj = {
        "<class 'function'>": 'function',
        "<class 'int'>": 'int',
        "<class 'str'": 'str',
        "<class 'generator'>": 'generator',
        "<class '__main__.": 'class',
        "<class 'type'>": 'class'
    }
    dict_func = {
        'function': 'obj.__doc__; '
                    'inspect.getfullargspec(obj); '
                    'inspect.getsourcelines(obj)',
        'generator': 'inspect.getgeneratorstate(obj)',
        'int': 'isinstance(obj, int)',
        'str': 'isinstance(obj, str)',
        'class': 'inspect.isclass(obj); '
                 'obj.__doc__; '
                 'obj.__dict__; '
                 'get_all_methods_details(obj)'
    }
    name_object = [n for n in g if id(g[n]) == id(obj)][0]
    print(f'Исследуем объект: {name_object}')
    # print(type(obj))
    for i in dict_obj:
        if i in str(type(obj)):
            print('Тип: ', dict_obj[i])
            list_commands = dict_func[dict_obj[i]].split(';')
            for j in list_commands:
                print(f'Значение каманды: {j}: ', eval(j))
                # print('eval: ', eval(dict_func[dict_obj[i]]))

    if callable(obj):
        print(f'Объект {obj.__name__} является вызываемым')
        sig = signature(obj)
        print(f'Принимает параметры: {sig}')
    print('*' * 20, '\n')


my_obj = MyClass(5)
my_int = 20
my_str = 'jhgjhg gjhg'
gen1 = my_func_gen()

introspection_info(MyClass)
introspection_info(my_func)
introspection_info(my_obj)
introspection_info(my_int)
introspection_info(my_str)


introspection_info(gen1)
gen1.__next__()
introspection_info(gen1)
