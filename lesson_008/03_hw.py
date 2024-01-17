# Импортируйте модуль warnings.
# Реализуйте функцию для расчёта деления, которая будет генерировать предупреждение, если делитель близок к нулю
# (например, меньше 0.01), предупреждая об опасности деления на ноль.
# Сгенерируйте UserWarning в этом случае.
# Используйте разные фильтры для управления поведением программы при появлении такого предупреждения: always,
# ignore, error
#
#
# Комментарии к заданию:
#
# Предупреждения часто используются для информирования о ситуациях, которые не являются критическими ошибками,
# но могут привести к потенциальным проблемам (например, устаревание использованного API или непредвиденное
# использование функции).
# В отличие от исключений, предупреждения не останавливают выполнение программы, но предоставляют полезную информацию
# разработчикам.

import warnings


def war_level(warn):
    if warn > 1:
        warnings.simplefilter('ignore')
        print('warning ignore')
    elif 0.001 < warn <= 0.01:
        warnings.simplefilter('always')
        print('warning always')
    elif warn <= 0.001:
        warnings.simplefilter('error')
        print('warning error')


def func_dev(a, b):
    c = a / b
    war_level(c)
    if c <= 0.01:
        warnings.warn(f'Аааааааа, скоро ноль, уже {c}')


for i in range(100, 10000, 200):
    try:
        func_dev(1, i)
    except UserWarning:
        print('Все, приехали')

# D:\Python\Python39\python.exe D:\Python\Projects\UU\lessons\lesson_008\03_hw.py
# warning always
# D:\Python\Projects\UU\lessons\lesson_008\03_hw.py:36: UserWarning: Аааааааа, скоро ноль, уже 0.01
#   warnings.warn(f'Аааааааа, скоро ноль, уже {c}')
# D:\Python\Projects\UU\lessons\lesson_008\03_hw.py:36: UserWarning: Аааааааа, скоро ноль, уже 0.0033333333333333335
#   warnings.warn(f'Аааааааа, скоро ноль, уже {c}')
# D:\Python\Projects\UU\lessons\lesson_008\03_hw.py:36: UserWarning: Аааааааа, скоро ноль, уже 0.002
#   warnings.warn(f'Аааааааа, скоро ноль, уже {c}')
# D:\Python\Projects\UU\lessons\lesson_008\03_hw.py:36: UserWarning: Аааааааа, скоро ноль, уже 0.0014285714285714286
#   warnings.warn(f'Аааааааа, скоро ноль, уже {c}')
# D:\Python\Projects\UU\lessons\lesson_008\03_hw.py:36: UserWarning: Аааааааа, скоро ноль, уже 0.0011111111111111111
#   warnings.warn(f'Аааааааа, скоро ноль, уже {c}')
# warning always
# warning always
# warning always
# warning always
# warning error
# Все, приехали
# warning error
# Все, приехали
# warning error
# ...