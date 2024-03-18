import csv
import re

travel_notes = []


def write_holiday_cities(first_letter):
    with open('../data/travel-notes.csv', 'r', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            travel_notes.append(row)
            print(row)
    print(travel_notes, '\n')

    name = []
    set_cities_for_vist = set()
    for i in range(len(travel_notes)):
        name.append(travel_notes[i][0])
    list_name = [search_name for search_name in name if re.findall(rf'[{first_letter}]\w+', search_name)]

    set_cities_visited = set()

    print(list_name)
    patern = r'(?:(?:[^,]*\[[^][]*])+[^,]*|[^,]+)'
    patern_1 = r"(?:[^';]*\[[^][]*])+[^';]*|[^';]+"
    for i, j in enumerate(list_name):
        cities = re.findall(patern, travel_notes[i][1])
        for city in re.findall(patern_1, cities[0]):
            set_cities_visited.add(city)
        cities = re.findall(patern, str(travel_notes[i][2]))
        for city in re.findall(patern_1, cities[0]):
            set_cities_for_vist.add(city)

    print(sorted(set_cities_visited))
    print(sorted(set_cities_for_vist))


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