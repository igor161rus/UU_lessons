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
    list_ext = ['.jpg', '.jpeg', '.png', '.gif']
    urls = re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+])(?:[^'>])+", html_text)
    # print(urls)

    image_links = []
    for url in urls:
        for ext in list_ext:
            if url.endswith(ext):
                image_links.append(url)
    # print(image_links)
    return image_links


def extract_image_links_v2(html_text):
    """Версия в которой сразу отбираются нужные расширения"""
    pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+])(?:[^'>])+(?:jpg|png|gif|jpeg)"
    urls = re.findall(pattern, html_text)
    return urls


sample_html = ("<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'> "
               "<img src='https://example.com/image3.gif'> <src='https://example.com/image3.py'>"
               "<img src='http://example.com/image4.jpeg'> <img src='https://example.com/image4.zip'>"
               "<img src='https://example.com/image3.txt'> <src='https://example.com/image3.jpe'>")


# sample_html = ("<img src='https://example.com/image4.zip'>")

def print_result(list_image_links):
    if list_image_links:
        for image_link in list_image_links:
            print(image_link)
    else:
        print("Нет ссылок с картинками в HTML тексте.")


print_result(extract_image_links(sample_html))
print('\n', '*' * 10, 'v2', '*' * 10)
print_result(extract_image_links_v2(sample_html))

# image_links = extract_image_links(sample_html)
# if image_links:
#     for image_link in image_links:
#         print(image_link)
# else:
#     print("Нет ссылок с картинками в HTML тексте.")


# Результат
# D:\Python\Python312\python.exe D:\Python\Projects\UU\lessons\lesson_014\hw_02.py
# https://example.com/image1.jpg
# http://example.com/image2.png
# https://example.com/image3.gif
# http://example.com/image4.jpeg
#
#  ********** v2 **********
# https://example.com/image1.jpg
# http://example.com/image2.png
# https://example.com/image3.gif
# http://example.com/image4.jpeg
#
# Process finished with exit code 0


# D:\Python\Python312\python.exe D:\Python\Projects\UU\lessons\lesson_014\hw_02.py
# Нет ссылок с картинками в HTML тексте.
#
#  ********** v2 **********
# Нет ссылок с картинками в HTML тексте.
#
# Process finished with exit code 0
