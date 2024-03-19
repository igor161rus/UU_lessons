import json

data = {
    "FirstName": "Egor",
    "LastName": "Ivanov",
    "Address": {
        "City": "Moscow",
        "Street": "Lenina",
    },
    "ContactDetails": {
        "Email": "a@a.ru",
        "Phone": "123",
    }
}

with open('data.json', 'w') as f:
    json.dump(data, f)

json_data = json.dumps(data)
print(json_data)

json_data_i = json.dumps(data, indent=4)
print(json_data_i)
with open('data_i.json', 'w') as f:
    f.write(json_data_i)

json_data_sorted = json.dumps(data, indent=4, sort_keys=True)
print(json_data_sorted)
print('-------------------\n')

with open('data_i.json', 'r') as f:
    data_i = json.load(f)
print(data_i)
print(data_i['FirstName'])
print({data_i['Address']['Street']})
print('-------------------\n')

loaded_json = json.loads(json_data)
print(loaded_json)
print('-------------------\n')

with open('todo.json', 'r') as f:
    todo = json.load(f)
number_of_tasks = len(todo)
print(number_of_tasks)
print(todo[0])

# количество пользователей
uniq_set_users = set()
for task in range(number_of_tasks):
    uniq_set_users.add(todo[task]['user_id'])
print(len(uniq_set_users))
print('-------------------\n')

# количество задач и количество выполненных задач
users = {}
for task in range(number_of_tasks):
    users[todo[task]['user_id']] = {'id': 0, 'is_complete': 0}
for task_number in range(number_of_tasks):
    users[todo[task_number]['user_id']]['id'] += 1
    if todo[task_number]['is_complete'] is True:
        users[todo[task_number]['user_id']]['is_complete'] += 1
print(users[1]['id'], users[1]['is_complete'])

with open('users.json', 'w') as f:
    json.dump(users, f, indent=4)
