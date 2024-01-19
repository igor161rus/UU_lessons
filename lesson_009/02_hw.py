# Теоретический комментарий:
# 1. Динамическое определение функций (def):
# В Python можно определять функции внутри других функций. Такие функции могут создаваться и возвращаться.
# Это основа для создания "фабрик функций" - функций, создающих функции.
#
# 2. Лямбда-функции:
# Лямбда-функции в Python — это анонимные функции, определённые одной строкой.
# Они удобны для создания простых функций на лету, особенно когда функция нужна временно или
# для одноразового использования.
#
# 3. Вызываемые объекты (__call__):
# В Python у класса может быть метод __call__, что позволяет его экземплярам вести себя как функции.
# Это дает возможность создавать объекты, которые могут быть вызваны как функции и хранить состояние между вызовами.
# Задание:
# Задача 1: Фабрика Функций
# Написать функцию, которая возвращает различные математические функции (например, деление, умножение)
# в зависимости от переданных аргументов.
#
# Задача 2: Лямбда-Функции
# Использовать лямбда-функцию для реализации простой операции и написать такую же функцию с использованием def.
# Например, возведение числа в квадрат
#
# Задача 3: Вызываемые Объекты
# Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__, который возвращает площадь прямоугольника, то есть a*b.
#
# Комментарии к заданию:
# Фабрика функций для сложения и вычитания:
# def create_operation(operation):
#     if operation == "add":
#         def add(x, y):
#             return x + y
#         return add # возвращаем функцию, как объект!! Тут скобки не нужны
#     elif operation == "subtract":
#         def subtract(x, y):
#             return x - y
#         return subtract
# my_func_add = create_operation("add")
# print(my_func_add(1,2))
#
# Пример лямбда функции с аналогом через def
# multiply = lambda x, y: x * y
# print(multiply(2, 3)) # Выводит 6
#
# def multiply_def(x, y):
#    return x * y
# print(multiply_def(2, 3)) # Выводит 6
#
# Пример создания вызываемого объекта
# class Repeater:
#    def __init__(self, value):
#        self.value = value
#    def __call__(self, n):
#        return [self.value] * n
#
# repeat_five = Repeater(5)
# print(repeat_five(3)) # Выводит [5, 5, 5]
#
# Пример вывода программы
# Задача 1: Фабрика функций
# 6
# 2.0
# Error: Division by zero
# Задача 2 лямбда
# 16
# 16
# Задача 3: Вызываемые oбъекты
# Стороны: 2, 4
# Площадь: 8

class CountDataException(Exception):
    """Класс CountDataException"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f'Ошибка класса CountDataException: {self.message}'


class InvalidDataException(Exception):
    """Класс InvalidDataException"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f'Ошибка класса InvalidDataException: {self.message}'


def enter_data():
    """ Функция ввода данных
    Запрашивает числа и операцию. Формирует список из чисел и операции
    """
    list_input_data = list(input('Введите через пробел два числа и операцию: ').split())
    list_data = []
    for i, j in enumerate(list_input_data):
        if i < 2:
            try:
                list_data.append(int(j))
            except ValueError:
                try:
                    list_data.append(float(j))
                except ValueError:
                    raise InvalidDataException(f'Введен не верный аргумент {j}')
        elif i == 2:
            list_data.append(j)
        else:
            raise CountDataException(f'Введено не верное число аргументов: {len(list_input_data)}, необходимо 3')
    return list_data


def create_operation(operation):
    if operation == "умножение":
        def multiplication(list_num):
            return f'{operation} {list_num[0]} на {list_num[1]} = {list_num[0] * list_num[1]}'

        return multiplication  # возвращаем функцию, как объект!! Тут скобки не нужны
    elif operation == "деление":
        def division(list_num):
            try:
                return f'{operation} {list_num[0]} на {list_num[1]} = {list_num[0] / list_num[1]}'
            except ZeroDivisionError:
                return f'Ошибка, {operation} {list_num[0]} на {list_num[1]} - деление на 0'

        return division


# a, b, c = map(int, input('Введите через пробел два числа и операцию: ').split())
try:
    calc_data = enter_data()
    my_calculator = create_operation(calc_data[2])
    list_num = [x for x in calc_data if isinstance(x, (int, float))]
    res = my_calculator(list_num)
    print(res)
except (InvalidDataException, CountDataException) as err:
    print(f'{err}')


