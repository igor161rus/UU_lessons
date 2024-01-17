# Задание:
#
# Создайте новый проект или продолжите работу в текущем проекте.
# Создайте минимум два своих собственных исключения, наследуя их от класса Exception.
# Например, InvalidDataException и ProcessingException.
# Напишите функцию, которая генерирует различные исключения в зависимости от передаваемых ей аргументов.
# Добавьте обработку исключений в функции, вызывающие вашу функцию, и передайте исключения дальше по стеку вызовов.
# В основной части программы вызовите эти функции и корректно обработайте
#
# Комментарии к заданию:
#
# Важно понять разницу между обработкой исключений (блок try/except) и их генерацией (оператор raise).
# Дополнительно: попробуйте использовать блоки finally или else для дополнительных действий при обработке исключений.
# Обратите внимание на то, как исключения передаются по стеку вызовов и как это можно использовать
# для стратегии обработки ошибок в сложных программах.
# Важно!! Для передачи обработанных исключений в вызвавшую функцию, нужно вызывать raise

class InvalidDataException(Exception):
    """Класс InvalidDataException"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f'Ошибка класса InvalidDataException: {self.message}'


class ProcessingException(Exception):
    """Класс ProcessingException"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f'Ошибка класса ProcessingException: {self.message}'


def func_1(a, b):
    c = a / b
    if a > b:
        raise InvalidDataException('Ошибка в функции func_1')
    elif c < b:
        raise ProcessingException('Ошибка в функции func_1')
    else:
        return c


def func_2():
    try:
        a, b = map(int, input('Введите через пробел два числа: ').split())
        c = func_1(a, b)
    except ValueError as exc:
        print(f'Не верное значение {exc}')
    except InvalidDataException as err:
        print(f'Ошибка func_2 {err}')
    except ProcessingException as err:
        print(f'Ошибка func_2 {err}')
    else:
        print(f'В функции func_2 ошибок нет, результат {c}')

try:
    func_2()
    print('В main ошибок не долетело') # Выведет если не будет исключений или они обработаны выше в стеке
except InvalidDataException as exc:
    print(f'Ошибка, {exc}')
else:
    print('Ошибок нет, main') # Выведет 'Ошибок нет' если не будет исключений, в нашем случае они обработаны в func_2
finally:
    print('Домашнее задание по теме "Создание исключений"') # Выполнится всегда

# 1
# D:\Python\Python39\python.exe D:\Python\Projects\UU\lessons\lesson_008\02_hw.py
# Введите через пробел два числа: 5 5
# Ошибка func_2 Ошибка класса ProcessingException: Ошибка в функции func_1
# В main ошибок не долетело
# Ошибок нет, main
# Домашнее задание по теме "Создание исключений"

# 2
# D:\Python\Python39\python.exe D:\Python\Projects\UU\lessons\lesson_008\02_hw.py
# Введите через пробел два числа: 10 5
# Ошибка func_2 Ошибка класса InvalidDataException: Ошибка в функции func_1
# В main ошибок не долетело
# Ошибок нет, main
# Домашнее задание по теме "Создание исключений"

# 3
# D:\Python\Python39\python.exe D:\Python\Projects\UU\lessons\lesson_008\02_hw.py
# Введите через пробел два числа: 1 1
# В функции func_2 ошибок нет, результат 1.0
# В main ошибок не долетело
# Ошибок нет, main
# Домашнее задание по теме "Создание исключений"