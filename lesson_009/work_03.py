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

