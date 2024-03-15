import csv

inv = []

with open('work_06.csv', 'r', newline='') as csv_file:
    csv_data = csv.reader(csv_file)
    for row in csv_data:
        inv.append(row)
print(inv)

new_inv = ['bjkjnmbjhjh', '1935', '3']
with open('work_06.csv', 'a', newline='') as out_csv:
    csv_writer = csv.writer(out_csv)
    csv_writer.writerow(new_inv)