# Добавление обработки исключений. К данным функциям добавить как минимум одну обработку указанных типов исключений:
# def string_to_int(s): # добавить обработку ValueError
#    return int(s)
# def read_file(filename): # добавить обработку FileNotFoundError, IOError
# with open(filename, 'r') as file:
#    return file.read()
# def divide_numbers(a, b): # добавить обработку ZeroDivisionError, TypeError
#     return a / b
# def access_list_element(lst, index): # добавить обработку IndexError, TypeError
#     return lst[index]

s = input()


def string_to_int(s):  # добавить обработку ValueError
    try:
        return int(s)
    except ValueError as exc:
        return f'Ошибка: {exc}, невозможно преобразовать "{s}" в функции {string_to_int.__name__}'


def read_file(filename):  # добавить обработку FileNotFoundError, IOError
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ''
    except IOError:
        return ''


def divide_numbers(a, b):  # добавить обработку ZeroDivisionError, TypeError
    return a / b


def access_list_element(lst, index):  # добавить обработку IndexError, TypeError
    return lst[index]


print(string_to_int(s))
