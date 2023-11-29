def my_function_1(a=1, b=2, c=3):
    """Функция с тремя целочисленными параметрами по-умолчанию"""
    print(f'Параметры функции:\n a = {a}\n b = {b}\n c = {c}\n')


def my_func_str(a='A', b='B', c='C'):
    """Функция с тремя строковыми параметрами по-умолчанию"""
    print(f'Параметры функции:\n a = {a}\n b = {b}\n c = {c}\n')


my_function_1(a=5)
my_function_1(b=6)
my_function_1(c=7)
my_function_1(a=5, b=8, c=10)

my_func_str(a='Aa')
my_func_str(b='Bb')
my_func_str(c='Cc')
my_func_str(a='AA', b='BB', c='CC')

# Распаковка параметров:
my_list = [10, 20, 30]
my_function_1(*my_list)


# Результат

# D:\Python\Python39\python.exe D:\Python\Projects\UU\lessons\lesson_003\02_function_param.py
# Параметры функции:
#  a = 5
#  b = 2
#  c = 3
#
# Параметры функции:
#  a = 1
#  b = 6
#  c = 3
#
# Параметры функции:
#  a = 1
#  b = 2
#  c = 7
#
# Параметры функции:
#  a = 5
#  b = 8
#  c = 10
#
# Параметры функции:
#  a = Aa
#  b = B
#  c = C
#
# Параметры функции:
#  a = A
#  b = Bb
#  c = C
#
# Параметры функции:
#  a = A
#  b = B
#  c = Cc
#
# Параметры функции:
#  a = AA
#  b = BB
#  c = CC
#
# Параметры функции:
#  a = 10
#  b = 20
#  c = 30
