# Добавление обработки исключений. К данным функциям добавить как минимум одну обработку указанных типов
# исключений:
# def string_to_int(s): # добавить обработку ValueError
#    return int(s)
# def read_file(filename): # добавить обработку FileNotFoundError, IOError
# with open(filename, 'r') as file:
#    return file.read()
# def divide_numbers(a, b): # добавить обработку ZeroDivisionError, TypeError
#     return a / b
# def access_list_element(lst, index): # добавить обработку IndexError, TypeError
#     return lst[index]
import os


def string_to_int(s):  # добавить обработку ValueError
    try:
        return int(s)
    except ValueError as exc:
        return f'Ошибка: {exc}, невозможно преобразовать "{s}" в функции {string_to_int.__name__}'


def read_file(filename):  # добавить обработку FileNotFoundError, IOError
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError as exc:
        return f'Ошибка: {exc}, файл не найден'
    except IOError as exc:
        return f'Ошибка: {exc} при работе с файлом {filename}'


def divide_numbers(a, b):  # добавить обработку ZeroDivisionError, TypeError
    try:
        return a / b
    except ZeroDivisionError as exc:
        return f'Ошибка {exc} при делении {a} на {b}'
    except TypeError as exc:
        return f'Ошибка {exc}, не верный тип данных'


def access_list_element(lst, index):  # добавить обработку IndexError, TypeError
    try:
        return lst[index]
    except IndexError as exc:
        return f'Ошибка {exc} нет такого индекса {index} в списке {lst}'
    except TypeError as exc:
        return f'Ошибка {exc}, не верный индекс: {index}'


# 1
s = input('string_to_int(s): ')
print(string_to_int(s))
# string_to_int(s): jhgf
# Ошибка: invalid literal for int() with base 10: 'jhgf', невозможно преобразовать "jhgf" в функции string_to_int

# 2
filename = input('read_file(filename): ')
print(read_file(filename))
# Ошибка: [Errno 2] No such file or directory: 'test.tx', файл не найден

# 3
a = input('Введите a: ')
b = input('Введите b: ')
print(divide_numbers(a, b))
print(divide_numbers(int(a), int(b)))
# Введите a: 10
# Введите b: 0
# Ошибка unsupported operand type(s) for /: 'str' and 'str', не верный тип данных
# Ошибка division by zero при делении 10 на 0

# 4
lst = []
path = os.path.dirname(__file__)
for filenames in os.walk(path):
    lst = filenames[2]
print(lst)
print(access_list_element(lst, 1))
print(access_list_element(lst, 10))
print(access_list_element(lst, '1'))
# ['01_hw.py', 'test.txt', 'work_2.py', 'work_3.py']
# test.txt
# Ошибка list index out of range нет такого индекса 10 в списке ['01_hw.py', 'test.txt', 'work_2.py', 'work_3.py']
# Ошибка list indices must be integers or slices, not str, не верный индекс: 1

