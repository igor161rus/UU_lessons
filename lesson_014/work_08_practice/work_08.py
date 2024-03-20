import csv
import json
import re
from collections import defaultdict
from datetime import datetime
from decimal import Decimal, ROUND_HALF_EVEN
from pprint import pprint

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

result_formatted = [{
    'date': record['date'].strftime('%d.%m.%Y'),
    'city': record['city'],
    'expanses': str(record['expanses'].quantize(Decimal('1.00'), ROUND_HALF_EVEN))

}
    for record in result
]
pprint(result_formatted)

with open('data/PBDetail.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['date', 'city', 'expanses'])
    writer.writeheader()
    writer.writerows(result_formatted)

result_aggregated_temp = defaultdict(lambda: {'cities': set(), 'expanses_sum': Decimal(0),
                                              'month': '', 'date_for_sort': None})

for record in result:
    month_datetime = datetime(year=record['date'].year, month=record['date'].month, day=1)
    month = month_datetime.strftime('%m-%Y')
    result_aggregated_temp[month]['cities'].add(record['city'])
    result_aggregated_temp[month]['expanses_sum'] += record['expanses']
    result_aggregated_temp[month]['month'] = month
    result_aggregated_temp[month]['date_for_sort'] = month_datetime

pprint(result_aggregated_temp)

result_aggregated = sorted(result_aggregated_temp.values(), key=lambda x: x['date_for_sort'])

result_aggregated_formated = [{
    'month': record['month'],
    'cities': ', '.join(record['cities']),
    'expanses_sum': str(record['expanses_sum'].quantize(Decimal('1.00'), ROUND_HALF_EVEN))
}
    for record in result_aggregated
]
pprint(result_aggregated_formated)

with open('data/PBMonth.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['month', 'cities', 'expanses_sum'])
    writer.writeheader()
    writer.writerows(result_aggregated_formated)








