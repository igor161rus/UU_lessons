import csv
import re

travel_notes = []


def write_holiday_cities(first_letter):
    set_cities_for_visit = set()
    set_cities_visited = set()
    dict_visit = {}
    dict_visited = {}
    name = []
    with open('../data/travel-notes.csv', 'r', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            patern = r"\w+(?:(?:[^;]*\[[^][]*])+[^;]*|[^;']+)"
            travel_notes.append(row)
            cities = re.findall(patern, row[2])
            for city in cities:
                set_cities_for_visit.add(city)
            dict_visit[row[0]] = cities
            cities = re.findall(patern, row[1])
            for city in cities:
                set_cities_visited.add(city)
            dict_visited[row[0]] = cities

        # set_cities_for_visit_potok = set_cities_for_visit - set_cities_visited
        set_cities_all = set_cities_for_visit | set_cities_visited

    for i in range(len(travel_notes)):
        name.append(travel_notes[i][0])
    list_name = [search_name for search_name in name if re.findall(rf'[{first_letter}]\w+', search_name)]

    set_cities_visited.clear()
    set_cities_for_visit.clear()
    for i in list_name:
        for city in dict_visited[i]:
            set_cities_visited.add(city)
        for city in dict_visit[i]:
            set_cities_for_visit.add(city)

    # patern = r'(?:(?:[^,]*\[[^][]*])+[^,]*|[^,]+)'
    # patern_1 = r"(?:[^';]*\[[^][]*])+[^';]*|[^';]+"
    # for i, j in enumerate(list_name):
    #     cities = re.findall(patern, travel_notes[i][1])
    #     for city in re.findall(patern_1, cities[0]):
    #         set_cities_visited.add(city)
    #     cities = re.findall(patern, str(travel_notes[i][2]))
    #     for city in re.findall(patern_1, cities[0]):
    #         set_cities_for_vist.add(city)

    with open('../data/holiday.csv', 'w', newline='', encoding='utf-8') as out_csv:
        csv_writer = csv.writer(out_csv, delimiter=',')
        csv_writer.writerow([f'# Информация о городах людей имена которых начинаются на {first_letter}'])
        csv_writer.writerow(['# '] + [", ".join(list_name)])
        # csv_writer.writerows([['Посетили'], ['Хотят посетить'], ['Никогда не были в'], ['Следующим городом будет']])

        csv_writer.writerow([f'Посетили:'] + sorted(set_cities_visited))
        csv_writer.writerow([f'Хотят посетить:'] + sorted(set_cities_for_visit))
        csv_writer.writerow([f'Никогда не были в:'] + sorted(set_cities_all - set_cities_visited))
        csv_writer.writerow([f'Следующим городом будет:'] + [str(sorted(set_cities_for_visit)[0])])
        csv_writer.writerow([f'Рекомендуем посетить:'] + [str(sorted(set_cities_all - set_cities_visited)[0])])


write_holiday_cities(first_letter='L')
