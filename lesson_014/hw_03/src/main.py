import csv
import re

travel_notes = []


def write_holiday_cities(first_letter):
    set_cities_for_vist = set()
    set_cities_visited = set()
    name = []
    with open('../data/travel-notes.csv', 'r', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            patern = r"\w+(?:(?:[^;]*\[[^][]*])+[^;]*|[^;']+)"
            travel_notes.append(row)
            cities = re.findall(patern, row[2])
            for city in cities:
                set_cities_for_vist.add(city)
            cities = re.findall(patern, row[1])
            for city in cities:
                set_cities_visited.add(city)
        set_cities_for_vist = sorted(set_cities_for_vist - set_cities_visited)
        print(set_cities_for_vist)
        # print(set_cities_for_vist)
    # print(travel_notes, '\n')

    for i in range(len(travel_notes)):
        name.append(travel_notes[i][0])
    list_name = [search_name for search_name in name if re.findall(rf'[{first_letter}]\w+', search_name)]

    print(list_name)
    patern = r'(?:(?:[^,]*\[[^][]*])+[^,]*|[^,]+)'
    patern_1 = r"(?:[^';]*\[[^][]*])+[^';]*|[^';]+"
    set_cities_visited.clear()
    for i, j in enumerate(list_name):
        cities = re.findall(patern, travel_notes[i][1])
        print(cities)
        for city in re.findall(patern_1, cities[0]):
            set_cities_visited.add(city)
            # set_cities_for_vist.remove(city)
        # cities = re.findall(patern, str(travel_notes[i][2]))
        # for city in re.findall(patern_1, cities[0]):
        #     set_cities_for_vist.add(city)

    print(sorted(set_cities_visited))
    print(sorted(set_cities_for_vist))

    with open('../data/holiday1.csv', 'w', newline='', encoding='utf-8') as out_csv:
        csv_writer = csv.writer(out_csv)
        csv_writer.writerow([f'Информация о городах людей имена которых начинаются на {first_letter}'])
        # csv_writer.writerows([['Посетили'], ['Хотят посетить'], ['Никогда не были в'], ['Следующим городом будет']])

        csv_writer.writerow([f'Посетили:']+sorted(set_cities_visited))
        csv_writer.writerow([f'Хотят посетить:']+sorted(set_cities_for_vist))
        csv_writer.writerow([f'Никогда не были в:']+sorted(set_cities_for_vist))
        # csv_writer.writerow([f'Следующим городом будет:']+sorted(set_cities_for_vist[0]))



write_holiday_cities(first_letter='R')
