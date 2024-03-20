import json
import re
from datetime import datetime
from decimal import Decimal

re_data = r'jbd(\d{6})'
re_city = r'jbc(\w+)jbc'
re_expenses = r'jbe(\d+\.\d+)jbe'

with open('data/Petrov-Bashirov.json', encoding='utf-8') as f:
    data = json.load(f)
print(data)
print(len(data))

dates = set()
cities = set()
for key, message in data.items():
    dates.add(re.search(re_data, message)[1])
    cities.add(re.search(re_city, message)[1])
print(dates)
print(cities)

exchanges = {
    'Рим': Decimal(1.2),
    'Брюсель': Decimal(1.2),
    'Осло': Decimal(1.2),
    'Бобруйск': Decimal(1.0),
    'Лондон': Decimal(2.0),
    'Прага': Decimal(1.2),
    'Токио': Decimal(0.7),
    'Париж': Decimal(1.2),
    'Варшава': Decimal(1.2),
    'Стамбул': Decimal(0.5)
}


def data_str_to_datetime(data_str):
    return datetime.strptime(data_str, '%d%m%y')


def expenses_str_to_decimal(expenses_str, city):
    return Decimal(expenses_str) * exchanges[city]


result = []
for key, message in data.items():
    data_str = re.search(re_data, message)[1]
    city = re.search(re_city, message)[1]
    expenses_str = re.search(re_expenses, message)[1]

    result.append({
        'date': data_str_to_datetime(data_str),
        'city': city,
        'expanses': expenses_str_to_decimal(expenses_str, city),
    })
print(result)
result = sorted(result, key=lambda x: x['date'])
print(result)
