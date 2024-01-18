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
