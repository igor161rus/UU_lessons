import csv
import re

travel_notes = []


def write_holiday_cities(first_letter):
    with open('../data/travel-notes.csv', 'r', newline='', encoding='utf-8') as csv_file:
        # dialect = csv.Sniffer().sniff(csv_file.readline()), [',', ';']
        # csv_file.seek(0)
        # reader = csv.reader(csv_file, dialect=dialect)
        # print(dialect)
        # print(reader)
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            travel_notes.append(row)
            print(row)
    print(travel_notes)

    name = []
    for i in range(len(travel_notes)):
        name.append(travel_notes[i][0])
    list_name = [search_name for search_name in name if re.findall(rf'[{first_letter}]\w+', search_name)]
    cities_want_vist = [name for name in travel_notes if name[0] in list_name]
    print(cities_want_vist)
    print(list_name)

    with open('../data/holiday.csv', 'w', newline='', encoding='utf-8') as out_csv:
        csv_writer = csv.writer(out_csv)
        for row in travel_notes:
            if row[0].startswith(first_letter):
                csv_writer.writerow(row)


    # with open('../data/holiday.csv', 'w', newline='', encoding='utf-8') as out_csv:
    #     csv_writer = csv.writer(out_csv)
    #     for row in travel_notes:
    #         if row[0].startswith(first_letter):
    #             csv_writer.writerow(row)

write_holiday_cities(first_letter='L')