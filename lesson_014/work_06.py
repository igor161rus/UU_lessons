import csv

# inv = []
#
# with open('work_06.csv', 'r', newline='', encoding='utf-8') as csv_file:
#     dialect = csv.Sniffer().sniff(csv_file.readline()), [',', ';']
#     csv_file.seek(0)
#     reader = csv.reader(csv_file, dialect=dialect)
#     print(dialect)
#     print(reader)
#     csv_data = csv.reader(csv_file)
#     for row in csv_data:
#         inv.append(row)
#         print(row)
# print(inv)
#
# new_inv = ['bjkjnmbjhjh', '1935', '3']
# with open('work_06.csv', 'a', newline='') as out_csv:
#     csv_writer = csv.writer(out_csv)
#     csv_writer.writerow(new_inv)

# list_art = []
# with open('work_06.csv', 'r') as csv_file:
#     reader = csv.DictReader(csv_file, delimiter=',')
#     for row in reader:
#         name = row['name']
#         list_art.append(name)
#         print(row)
# print(list_art)

# new_art = {'name': 'new art', 'date': '1938', 'quantity': '2'}
# with open('work_06.csv', 'a', newline='') as out_csv:
#     fieldnames = ['name', 'date', 'quantity']
#     csv_writer = csv.DictWriter(out_csv, delimiter=',', fieldnames=inv[0])
#     csv_writer.writerow(new_art)


# list_need = []
# with open('work_06_1.csv', 'r', newline='') as csv_file:
#     csv_data = csv.reader(csv_file)
#     for row in csv_data:
#         list_need.append(row)
# print(f'Стандартный набор: {list_need}')
#
# add_list_need = [{'name:': 'whip', 'price:': '100', 'quantity:': '5'},
#                  {'name:': 'hat', 'price:': '200', 'quantity:': '2'},
#                  {'name:': 'shoes', 'price:': '300', 'quantity:': '1'}]
#
# with open('work_06_1.csv', 'w', newline='') as out_csv:
#     writer = csv.DictWriter(out_csv, delimiter=',', fieldnames=list_need[0])
#     writer.writeheader()
#     writer.writerows(add_list_need)

act = []

with open('Activities.csv', 'r', encoding='cp1251') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=',')
    for row in reader:
        distance = row['Расстояние']
        act.append(distance)
print(act[:3])
