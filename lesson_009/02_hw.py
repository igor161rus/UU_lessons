# Задача 1: Фабрика Функций
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


try:
    calc_data = enter_data()
    my_calculator = create_operation(calc_data[2])
    list_num = [x for x in calc_data if isinstance(x, (int, float))]
    res = my_calculator(list_num)
    print(res)
except (InvalidDataException, CountDataException) as err:
    print(f'{err}')

# D:\Python\Python39\python.exe D:\Python\Projects\UU\lessons\lesson_009\02_hw.py
# Введите через пробел два числа и операцию: 2 45 умножение
# умножение 2 на 45 = 90

# D:\Python\Python39\python.exe D:\Python\Projects\UU\lessons\lesson_009\02_hw.py
# Введите через пробел два числа и операцию: 2.8 123 деление
# деление 2.8 на 123 = 0.02276422764227642

# D:\Python\Python39\python.exe D:\Python\Projects\UU\lessons\lesson_009\02_hw.py
# Введите через пробел два числа и операцию: 2 0 деление
# Ошибка, деление 2 на 0 - деление на 0

# D:\Python\Python39\python.exe D:\Python\Projects\UU\lessons\lesson_009\02_hw.py
# Введите через пробел два числа и операцию: в 25 умножение
# Ошибка класса InvalidDataException: Введен не верный аргумент в

# D:\Python\Python39\python.exe D:\Python\Projects\UU\lessons\lesson_009\02_hw.py
# Введите через пробел два числа и операцию: 2.5 45 4 умножение
# Ошибка класса CountDataException: Введено не верное число аргументов: 4, необходимо 3

# Задача 2: Лямбда-Функции
print('Возведение в степень')
a, b = map(int, input('Введите два целых числа через пробел: 1 основание, 2 показатель: ').split())
exp = lambda x, y: x ** y
print(exp(a, b))


def exp_1(x, y):
    return x ** y


print(exp_1(a, b))


# D:\Python\Python39\python.exe D:\Python\Projects\UU\lessons\lesson_009\02_hw.py
# Возведение в степень
# Введите два целых числа через пробел: 1 основание, 2 показатель: 5 3
# 125
# 125

# Задача 3: Вызываемые Объекты
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.area = 0

    def __call__(self):
        return self.a * self.b


area_sq = Rect(5, 6)
print(f'Площадь: {area_sq()}')
print('Стороны: ', area_sq.a, area_sq.b)

# 30