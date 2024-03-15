import csv

inv = []

with open('work_06.csv', 'r', newline='', encoding='utf-8') as csv_file:
    csv_data = csv.reader(csv_file)
    for row in csv_data:
        inv.append(row)
        print(row)
print(inv)
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

new_art = {'name': 'new art', 'date': '1938', 'quantity': '2'}
with open('work_06.csv', 'a', newline='') as out_csv:
    fieldnames = ['name', 'date', 'quantity']
    csv_writer = csv.DictWriter(out_csv, delimiter=',', fieldnames=inv[0])
    csv_writer.writerow(new_art)
