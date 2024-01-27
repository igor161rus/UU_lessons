# Задание:
# Напишите 2 функции:
# Функция которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и
# "Составное" в противном случае.

# Пример:
# result = sum_three(2, 3, 6)
# print(result)
#
# Результат консоли:
# Простое
# 11
#
# Примечание:
# Не забудьте написать внутреннюю функцию wrapper в is_prime
# Функция is_prime должна возвращать wrapper
# @is_prime - декоратор для функции sum_three


def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res % 2 == 0:
            print('Простое' if res == 2 else 'Составное')
            return res
        d = 3
        while d * d <= res and res % d != 0:
            d += 2
        print('Простое' if d * d > res else 'Составное')
        return res

    return wrapper


@is_prime
def sum_three(*args):
    """Функция вычесления суммы аргументов"""
    res = 0
    for arg in args:
        res += arg
    return res


result = sum_three(2, 3, 6)
print(result)

# result = sum_three(2, 3, 6)
# Простое
# 11

# result = sum_three(2, 3, 6, 5, 46)
# Составное
# 62
