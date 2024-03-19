import json


def employees_rewrite(sort_type):
    with open('../data/employees.json', 'r') as f:
        data = json.load(f)

    sorted_data = sorted(data['employees'], key=lambda x: x[sort_type])
    with open(f'../data/employees_{sort_type}_sorted.json', 'w') as f:
        json.dump(sorted_data, f, indent=4)


employees_rewrite('firstName')
employees_rewrite('lastName')
employees_rewrite('department')
employees_rewrite('salary')
