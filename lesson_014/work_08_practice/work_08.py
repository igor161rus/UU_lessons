import json
import re

re_data = r'jbd(\d{6})'
re_city = r'jbc(\w+)jbc'
re_expenses = r'jbe(\d+\.\d+)jbe'

with open('data/Petrov-Bashirov.json') as f:
    data = json.load(f)
print(data)
print(len(data))

dates = set()
for key, message in data.items():
    dates.add(re.search(re_data, message))
print(dates)
