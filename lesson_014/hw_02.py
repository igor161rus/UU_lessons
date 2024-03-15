# Задание:
#
# Разработайте функцию для извлечения информации из HTML-текста (строки Python) о ссылках на изображения (URL-адресах картинок). Функция должна находить все ссылки на изображения в форматах JPEG, JPG, PNG или GIF и возвращать их список.
#
# 1. Создайте функцию extract_image_links(html_text), которая принимает HTML-текст и извлекает ссылки на изображения.
# 2. Используйте регулярные выражения для поиска URL-адресов картинок с расширениями .jpg, .jpeg, .png или .gif.
# 3. Верните список всех найденных ссылок на изображения.
#
#
# Пример работы функции:
#
#
# sample_html = "<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'> <img src='https://example.com/image3.gif'>"
#
# image_links = extract_image_links(sample_html)
# if image_links:
#   for image_link in image_links:
#     print(image_link)
# else:
#   print("Нет ссылок с картинками в HTML тексте.")
#
# Вывод на консоль:
# https://example.com/image1.jpg
# http://example.com/image2.png
# https://example.com/image3.gif
#
# Примечания:
# Вам могут понадобится следующие спец. символы: / ? [] | +
# Учтите что 'http' это подстрока строки 'https'.
#
# Файл с исходным кодом прикрепите к домашнему заданию.

# regex101.com
# https://docs.python.org/3/library/re.html

import re


def extract_image_links(html_text):
    # urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html_text)
    urls = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+])(?:[^'>])+", html_text)
    print(urls)
    # if match:
    #     print(match.group(1))



sample_html = "<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'> <img src='https://example.com/image3.gif'>"

extract_image_links(sample_html)

# image_links = extract_image_links(sample_html)
# if image_links:
#     for image_link in image_links:
#         print(image_link)
# else:
#     print("Нет ссылок с картинками в HTML тексте.")
