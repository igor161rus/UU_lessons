import requests as rq
import bs4 as bs

response = rq.get("https://ya.ru")
soup = bs.BeautifulSoup(response.text, "html.parser")
result = soup.find_all("span")
print(result)