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


def my_function(a, b, c):
    if c:
        c = a / b
        print(c)
    else:
        try:
            c = a / b
            print(c)
        except ZeroDivisionError as exc:
            print(f'Ошибка {exc} при делении {a} на {b}')


try:
    my_function(2, 0, True)
    print('ok')
except:
    raise InvalidDataException('Деление на ноль')
finally:
    print('Домашнее задание по теме "Создание исключений"')
