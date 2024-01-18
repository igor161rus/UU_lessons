from pprint import pprint


def get_multiplier_v1(n):
    if n == 2:
        def multiplier(x):
            return x * 2
    elif n == 3:
        def multiplier(x):
            return x * 3
    else:
        raise Exception('Я могу сделать умножители только на 2 или 3')
    return multiplier


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
by_2 = get_multiplier_v1(2)
by_3 = get_multiplier_v1(3)
result = map(by_2, my_numbers)
print(list(result))
result = map(by_3, my_numbers)
print(list(result))


def get_multiplier_v2(n):
    def multiplier(x):
        return x * n

    return multiplier


by_5 = get_multiplier_v2(5)
print(by_5(x=42))
result = map(by_5, my_numbers)
print(list(result))
by_100 = get_multiplier_v2(100)
result = map(by_100, my_numbers)
print(list(result))
print()
print('***************************')
print()


def matrix(some_list):
    def multiply_column(x):
        res = []
        for element in some_list:
            res.append(element * x)
        return res

    return multiply_column


matrix_on_my_numbers = matrix(my_numbers)

they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
result = map(matrix_on_my_numbers, they_numbers)
print(list(result))
print(matrix_on_my_numbers(100))

my_numbers.extend([10, 20, 30])
result = map(matrix_on_my_numbers, they_numbers)
pprint(list(result))
print()
print('***************************')
print()

result = map(lambda x: x + 10, my_numbers)
print(list(result))

my_func = lambda x: x + 10
pprint(my_func(x=42))
print(type(my_func))
print()

print(my_numbers)
print(they_numbers)
result = map(lambda x, y: x + y, my_numbers, they_numbers)
print(list(result))
print()
print('***************************')
print()


class Multiplier:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x * self.n


by_100500 = Multiplier(n=100500)
result = by_100500(x=42)
print(result)

result = map(by_100500, my_numbers)
print(list(result))

print(callable(by_100500))
