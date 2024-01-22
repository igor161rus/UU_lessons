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
    j = 0
    len_str = len(in_str)
    for i in in_str:
        yield i
    while j < len_str-1:
        yield in_str[j] + in_str[j + 1]
        j += 1
    yield in_str


a = all_variants("abc")
for i in a:
    print(i)

# all_variants("abc")
# a
# b
# c
# ab
# bc
# abc


# all_variants("abcdef")
# a
# b
# c
# d
# e
# f
# ab
# bc
# cd
# de
# ef
# abcdef
