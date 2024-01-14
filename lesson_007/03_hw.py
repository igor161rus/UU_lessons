# Создайте новый проект или продолжите работу в текущем проекте.
# Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
# Примените os.path.join для формирования полного пути к файлам.
# Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
# Используйте os.path.getsize для получения размера файла.
# Используйте os.path.dirname для получения родительской директории файла.
#
# Комментарии к заданию:
#
# Ключевая идея – использование вложенного for
#
# for root, dirs, files in os.walk(directory):
#   for file in files:
#     filepath = ?
#     filetime = ?
#     formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#     filesize = ?
#     parent_dir = ?
#     print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
#
# Так как в разных операционных системах разная схема расположения папок, тестировать проще всего в папке проекта (directory = “.”)
# Пример возможного вывода:
# Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11, Родительская директория: .
#
# Пример решения:
#
# Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11, Родительская директория: .
# Пример кода:
import os, time

directory = os.path.dirname(__file__)
path_normalized = os.path.normpath(directory)
print(path_normalized)
# widows
# C:\Users\admin\AppData\Local\Programs\Python\Python311\python.exe E:\python\projects\UU_lessons\lesson_007\03_hw.py
# E:\python\projects\UU_lessons\lesson_007


# linux
# /usr/bin/python3.10 /home/ha/python/projects/UU_lessons/lesson_007/03_hw.py
# /home/ha/python/projects/UU_lessons/lesson_007

# for root, dirs, files in os.walk(directory):
#   for file in files:
#     filepath = ?
#     filetime = ?
#     formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#     filesize = ?
#     parent_dir = ?
#     print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
