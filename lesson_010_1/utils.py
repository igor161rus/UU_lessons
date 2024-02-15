import time


def time_track(func):
    def surrogate(*args, **kwargs):
        strted_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round(ended_at - strted_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate
