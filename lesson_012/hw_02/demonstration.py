import requests as rq
import bs4

# Пример 1. (Демонстрация работы запроса )

response = rq.get('https://www.youtube.com/') # (Запрос выполняется - 200)
soup = bs4.BeautifulSoup(response.text, 'lxml') # Составляется "суп" для парсинга

# Поиск всех тегов 'a' в html (супе) и вывод всех ссылок на экран с этого сайта
for tag in soup.find_all('a'):
    src = ''
    href = tag.get('href')
    if 'https' not in href:
        src = 'https://www.youtube.com'
    print(src + href)
