import time


def get_time_track(precision):
    def time_track(func):
        def surrogate(*args, **kwargs):
            strted_at = time.time()
            result = func(*args, **kwargs)
            ended_at = time.time()
            elapsed = round(ended_at - strted_at, 4)
            print(f'Функция работала {elapsed} секунд(ы)')
            return result
        return surrogate
    return time_track


def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))

time_track_precision_6 = get_time_track(precision=6)
digits = time_track_precision_6(digits)
result = digits()