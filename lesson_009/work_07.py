import time


def get_time_track(precision):
    print(f'получили точность, с которой надо выводить резудьтат - {precision}')
    print('начинаем создавать декоратор')
    def time_track(func):
        print(f'декоратор принял на вход функцию, которую надо отдекарировать - {func}')
        print('начинает создавать функцию-обертку')
        def surrogate(*args, **kwargs):
            print('мы в функции-обертке, которая заместит реальную функцию func ')
            print('засекаем время')
            strted_at = time.time()
            print('запускаем реальную функцию с переданными в функцию-обертку параметрами и заполняем результат')
            result = func(*args, **kwargs)
            print('определяем затраченное время')
            ended_at = time.time()
            print(f'вот тут-то и пригодится precision (== {precision} он запомнился в замыкании surogate))')
            elapsed = round(ended_at - strted_at, precision)
            print(f'Функция работала {elapsed} секунд(ы)')
            print('возвращаем результат, который вернула реальная функция')
            return result
        print('декоратор создал функцию-обертку и возвращает ее')
        return surrogate
    print('декоратор создан и пора его вернуть')
    return time_track


@get_time_track(precision=2)
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


# time_track_precision_6 = get_time_track(precision=6)
# digits = time_track_precision_6(digits)
result = digits(3141, 5926, 2718, 2818)
print(result)
