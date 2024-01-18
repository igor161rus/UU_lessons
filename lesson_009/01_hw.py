# Дан список целых чисел, примените функции map и filter так, чтобы в конечном списке оставить нечётные квадраты чисел
# Примечание
# Не забывайте, что встроенные функции map и filter возвращают генератор, сами операции преобразования не выполняются.
# Входные данные
# [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
# Выходные данные
# [1, 25, 49, 121, 1225, 7921]

def mul_by_2(x):
    return x ** 2


def is_odd(x):
    return x % 2


list1 = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
# res = map(mul_by_2, filter(is_odd, [y for y in list1 if y % 2]))
res = map(mul_by_2, filter(is_odd, list1))
print(list(res))

res = map(mul_by_2, [x for x in list1 if x % 2])
print(list(res))
