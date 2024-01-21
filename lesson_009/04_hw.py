# Задание
# Напишите функцию-генератор all_variants, которая будет возвращать все подпоследовательности переданной строки.
# В функцию передаётся только сама строка.
# Примечание
# Используйте оператор yield
# Входные данные
# a = all_variants("abc")
# for i in a:
# print(i)
# Выходные данные
# a
# b
# c
# ab
# bc
# abc

def all_variants(in_str):
    len_str = len(in_str)
    for i in range(len_str):
        for j in range(len_str - 1):
            yield in_str[i]


a = all_variants("abc")
for i in a:
    print(i)
