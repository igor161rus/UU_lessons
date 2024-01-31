# Задание:
# Напишите программу, которая создает два потока.
# Первый поток должен выводить числа от 1 до 10 с интервалом в 1 секунду.
# Второй поток должен выводить буквы от 'a' до 'j' с тем же интервалом.
# Оба потока должны работать параллельно.
#
# Примечание:
# Используйте методы: start() для старта потока, join() для заморозки дальнейшей интерпретации,
# пока процессы не завершаться.
# Для установки интервала в 1 секунду используйте функцию sleep() из модуля time, предварительно импортировав его.
#
#
# Входные данные:
# Нет
# Выходные данные:
# 1
# a
# 2
# b
# 3
# c
# ......
# 10
# j

import time
from threading import Thread, Lock

print_lock = Lock()

num_list = (i for i in range(1, 11))
letter_list = (chr(a) for a in range(97, 107))


def get_time_track(func):
    def wrapper(*args, **kwargs):
        strted_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round(ended_at - strted_at, 6)
        with print_lock:
            print(f'{func.__doc__} работала {elapsed} секунд(ы)')
        return result

    return wrapper


@get_time_track
def thread_numb():
    """Функция вывода букв от 'a' до 'j' с интервалом в 1 секунду"""
    for i in num_list:
        with print_lock:
            print(i, flush=True)
        time.sleep(1)


@get_time_track
def thread_letter():
    """Функция вывода букв от 'a' до 'j' с интервалом в 1 секунду"""
    for i in letter_list:
        with print_lock:
            print(i, flush=True)
        time.sleep(1)


thread_1 = Thread(target=thread_numb)
thread_2 = Thread(target=thread_letter)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()


# v2
@get_time_track
def func_out(nl):
    """Функция вывода цифр и букв"""
    if nl == 0:
        for i in num_list:
            print_lock.acquire()
            print(i, flush=True)
            print_lock.release()
            time.sleep(1)
    elif nl == 1:
        for i in letter_list:
            print_lock.acquire()
            print(i, flush=True)
            print_lock.release()
            time.sleep(1)


num_list = (i for i in range(1, 11))
letter_list = (chr(a) for a in range(97, 107))

for n in range(2):
    thread = Thread(target=func_out, args=(n,))
    thread.start()

thread.join()

# /usr/bin/python3.10 /home/ha/python/projects/UU_lessons/lesson_010/01_hw.py
# 1
# a
# b
# 2
# 3
# c
# 4
# d
# 5
# e
# 6
# f
# 7
# g
# 8
# h
# 9
# i
# 10
# j
# Функция вывода букв от 'a' до 'j' с интервалом в 1 секунду работала 10.012667 секунд(ы)
# Функция вывода букв от 'a' до 'j' с интервалом в 1 секунду работала 10.012957 секунд(ы)
# 1
# a
# 2
# b
# c
# 3
# d
# 4
# 5
# e
# 6
# f
# 7
# g
# 8
# h
# 9
# i
# 10
# j
# Функция вывода цифр и букв работала 10.012024 секунд(ы)
# Функция вывода цифр и букв работала 10.011941 секунд(ы)
