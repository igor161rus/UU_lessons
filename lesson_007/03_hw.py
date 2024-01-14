import os
import time

directory = os.path.dirname(__file__)
path_normalized = os.path.normpath(directory)
print(path_normalized)

for root, dirs, files in os.walk(path_normalized):
    for file in files:
        filepath = path_normalized
        filetime = time.time()

        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(__file__)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, '
              f'Размер: {filesize} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')

# windows:
# C:\Users\admin\AppData\Local\Programs\Python\Python311\python.exe E:\python\projects\UU_lessons\lesson_007\03_hw.py
# E:\python\projects\UU_lessons\lesson_007
# Обнаружен файл: 01_hw.py, Путь: E:\python\projects\UU_lessons\lesson_007, Размер: 318 байт, Время изменения: 14.01.2024 16:37, Родительская директория: E:\python\projects\UU_lessons\lesson_007
# Обнаружен файл: 02_hw.py, Путь: E:\python\projects\UU_lessons\lesson_007, Размер: 1968 байт, Время изменения: 14.01.2024 16:37, Родительская директория: E:\python\projects\UU_lessons\lesson_007
# Обнаружен файл: 03_hw.py, Путь: E:\python\projects\UU_lessons\lesson_007, Размер: 3149 байт, Время изменения: 14.01.2024 16:37, Родительская директория: E:\python\projects\UU_lessons\lesson_007
# Обнаружен файл: byron.txt, Путь: E:\python\projects\UU_lessons\lesson_007, Размер: 624 байт, Время изменения: 14.01.2024 16:37, Родительская директория: E:\python\projects\UU_lessons\lesson_007
# Обнаружен файл: hw_03.py, Путь: E:\python\projects\UU_lessons\lesson_007, Размер: 3388 байт, Время изменения: 14.01.2024 16:37, Родительская директория: E:\python\projects\UU_lessons\lesson_007
# Обнаружен файл: out.txt, Путь: E:\python\projects\UU_lessons\lesson_007, Размер: 5 байт, Время изменения: 14.01.2024 16:37, Родительская директория: E:\python\projects\UU_lessons\lesson_007
# Обнаружен файл: work.py, Путь: E:\python\projects\UU_lessons\lesson_007, Размер: 821 байт, Время изменения: 14.01.2024 16:37, Родительская директория: E:\python\projects\UU_lessons\lesson_007
# Обнаружен файл: work_2.py, Путь: E:\python\projects\UU_lessons\lesson_007, Размер: 341 байт, Время изменения: 14.01.2024 16:37, Родительская директория: E:\python\projects\UU_lessons\lesson_007
# Обнаружен файл: work_3.py, Путь: E:\python\projects\UU_lessons\lesson_007, Размер: 156 байт, Время изменения: 14.01.2024 16:37, Родительская директория: E:\python\projects\UU_lessons\lesson_007
# Обнаружен файл: work_4.py, Путь: E:\python\projects\UU_lessons\lesson_007, Размер: 647 байт, Время изменения: 14.01.2024 16:37, Родительская директория: E:\python\projects\UU_lessons\lesson_007
# Обнаружен файл: work_5.py, Путь: E:\python\projects\UU_lessons\lesson_007, Размер: 618 байт, Время изменения: 14.01.2024 16:37, Родительская директория: E:\python\projects\UU_lessons\lesson_007

# linux
# /usr/bin/python3.10 /home/ha/python/projects/UU_lessons/lesson_007/03_hw.py
# /home/ha/python/projects/UU_lessons/lesson_007
# Обнаружен файл: work_3.py, Путь: /home/ha/python/projects/UU_lessons/lesson_007, Размер: 151 байт, Время изменения: 14.01.2024 16:39, Родительская директория: /home/ha/python/projects/UU_lessons/lesson_007
# Обнаружен файл: hw_03.py, Путь: /home/ha/python/projects/UU_lessons/lesson_007, Размер: 3331 байт, Время изменения: 14.01.2024 16:39, Родительская директория: /home/ha/python/projects/UU_lessons/lesson_007
# Обнаружен файл: out.txt, Путь: /home/ha/python/projects/UU_lessons/lesson_007, Размер: 5 байт, Время изменения: 14.01.2024 16:39, Родительская директория: /home/ha/python/projects/UU_lessons/lesson_007
# Обнаружен файл: byron.txt, Путь: /home/ha/python/projects/UU_lessons/lesson_007, Размер: 607 байт, Время изменения: 14.01.2024 16:39, Родительская директория: /home/ha/python/projects/UU_lessons/lesson_007
# Обнаружен файл: work_4.py, Путь: /home/ha/python/projects/UU_lessons/lesson_007, Размер: 627 байт, Время изменения: 14.01.2024 16:39, Родительская директория: /home/ha/python/projects/UU_lessons/lesson_007
# Обнаружен файл: 01_hw.py, Путь: /home/ha/python/projects/UU_lessons/lesson_007, Размер: 309 байт, Время изменения: 14.01.2024 16:39, Родительская директория: /home/ha/python/projects/UU_lessons/lesson_007
# Обнаружен файл: 02_hw.py, Путь: /home/ha/python/projects/UU_lessons/lesson_007, Размер: 1947 байт, Время изменения: 14.01.2024 16:39, Родительская директория: /home/ha/python/projects/UU_lessons/lesson_007
# Обнаружен файл: 03_hw.py, Путь: /home/ha/python/projects/UU_lessons/lesson_007, Размер: 3723 байт, Время изменения: 14.01.2024 16:39, Родительская директория: /home/ha/python/projects/UU_lessons/lesson_007
# Обнаружен файл: work.py, Путь: /home/ha/python/projects/UU_lessons/lesson_007, Размер: 777 байт, Время изменения: 14.01.2024 16:39, Родительская директория: /home/ha/python/projects/UU_lessons/lesson_007
# Обнаружен файл: work_5.py, Путь: /home/ha/python/projects/UU_lessons/lesson_007, Размер: 598 байт, Время изменения: 14.01.2024 16:39, Родительская директория: /home/ha/python/projects/UU_lessons/lesson_007
# Обнаружен файл: work_2.py, Путь: /home/ha/python/projects/UU_lessons/lesson_007, Размер: 327 байт, Время изменения: 14.01.2024 16:39, Родительская директория: /home/ha/python/projects/UU_lessons/lesson_007
