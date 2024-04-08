from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://coinmarketcap.com/ru/'
response = requests.get(url).text

soup = BeautifulSoup(response, features='lxml')
for i in soup.findAll('tr')[1:]:
    name = i.findAll('td')[2].text
    # price = i.findAll('td')[4].text
    cap = i.findAll('td')[7].text

    # name = name.strip()
    # price = price.strip()
    # cap = cap.strip()

    print(name,  cap)

# pd.set_option('display.max_columns', None)
# aa = pd.read_html(url)
# # aa.to_csv('cmc.csv')
# print(aa)


def write_cmc_top():
    pass
