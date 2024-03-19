import json
import re


def employees_rewrite(sort_type):
    with open('../data/employees.json', 'r') as f:
        data = json.load(f)

    sort_type = sort_type.lower()
    if sort_type == 'lastname' or sort_type == 'firstname':
        sort_type = re.sub(r'n', 'N', sort_type.lower())

    if sort_type not in data['employees'][0]:
        raise ValueError('Bad key for sorting')
    if type(data['employees'][0][sort_type]) is str:
        sorted_data = sorted(data['employees'], key=lambda x: x[sort_type])
    elif type(data['employees'][0][sort_type]) is int:
        sorted_data = sorted(data['employees'], key=lambda x: x[sort_type], reverse=True)
    with open(f'../data/employees_{sort_type}_sorted.json', 'w') as f:
        json.dump(sorted_data, f, indent=4)


employees_rewrite('FirstName')
employees_rewrite('lastName')
employees_rewrite('department')
employees_rewrite('Salary')
