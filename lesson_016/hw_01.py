from bs4 import BeautifulSoup
import requests

response = requests.get('https://coinmarketcap.com/ru/')

if response.status_code == 200:
    html_doc = BeautifulSoup(response.text, features='html.parser')
    list_of_values = html_doc.find_all('span', {'class': "sc-aef7b723-0 LCOyB"})
    list_of_names = html_doc.find_all('a', {'href': '/ru/currencies/bitcoin/'})
    for names, values in zip(list_of_names, list_of_values):
        print(names.text, values.text)
else:
    print('Error')
def write_cmc_top():

    pass