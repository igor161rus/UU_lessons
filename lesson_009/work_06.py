def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


import time

strted_at = time.time()
result = digits(3141, 5926, 2718, 2818)
print(result)
ended_at = time.time()
elapsed = round(ended_at - strted_at, 4)
print(f'Функция работала {elapsed} секунд(ы)')


def time_track(func, *args, **kwargs):
    strted_at = time.time()
    result = func(*args, **kwargs)
    ended_at = time.time()
    elapsed = round(ended_at - strted_at, 4)
    print(f'Функция работала {elapsed} секунд(ы)')
    return result


result = time_track(digits, 3141, 5926, 2718, 2818)
print(result)
print()
print('*************************************')
print()


def time_track_v2(func):
    def surrogate(*args, **kwargs):
        strted_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round(ended_at - strted_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result

    return surrogate


timed_digits = time_track_v2(digits)
result = timed_digits(3141, 5926, 2718, 2818)
print(result)

digits = time_track_v2(digits)
result = digits(3141, 5926, 2718, 2818)
print(result)


@time_track_v2
def digits_v2(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


result = digits(3141, 5926, 2718, 2818)
print(result)

print()
print('*************************************')
print()
