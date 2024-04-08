from bs4 import BeautifulSoup
import requests

response = requests.get('https://yandex.ru/')

if response.status_code == 200:
    html_doc = BeautifulSoup(response.text, features='html.parser')
    # list_of_values = html_doc.find_all('span', {'class': 'inline-stock__value_inner'})
    list_of_values = html_doc.find_all('span', {'class': 'currency-rates__rateValue-2X'})
    # list_of_names = html_doc.find_all('a', {'class': 'home-link home-link_black_yes inline-stock__link'})
    list_of_names = html_doc.find_all('a', {'class': 'currency-rates__rate-fu'})

    for names, values in zip(list_of_names, list_of_values):
        print(names.text, values.text)
else:
    print('Error')
