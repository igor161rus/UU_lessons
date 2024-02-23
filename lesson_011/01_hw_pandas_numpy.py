import pandas
import numpy

# Series — одномерный массив
my_series = pandas.Series([5, 6, 7, 8, 9, 10])
print(my_series)
# Фильтрация данных массива по условию
print(my_series[my_series > 7])

# Данные получены numpy.arange(5), index - список меток.
s = pandas.Series(numpy.arange(5), index=['a', 'b', 'c', 'd', 'e'])
print(s, '\n')

# numpy.linspace(0, 1, 5) создаем массив от 0 до 1 (включая 1), равномерно разбитый на 5, те с приращением 0.25
# Series создает массив с данными 0.00, 0.25 - 1.00 и автоматическими метками от 0 до 4
s = pandas.Series(numpy.linspace(0, 1, 5))
print(s)

# Выбор элемента по его индексу
print(s[1])

# DataFrame работает с двумерными табличными данными
uu_lessons_dict = {'uu_lessons': ['lesson_8', 'lesson_9', 'lesson_10'],
                       'work': [5, 8, 5],
                       'home_work': [3, 5, 3]}
uu_lessons = pandas.DataFrame(uu_lessons_dict)
uu_lessons.index = ['Исключения', 'Инструменты функционального программирования', 'Мультипоточность']
print(uu_lessons)
print()
print('Количество уроков и домашних заданий в модуле Исключения')
print(uu_lessons.loc['Исключения'])

# Файл Activities.csv экспортирован из Garmin Connect
trainings = pandas.read_csv('Activities.csv')
print(trainings.head(10))

# Все поля представлены как строки, причем в колонке "Максимальная высота" высота больше 1000 м указана как 1,000
# Убираем запятую в колонке "Максимальная высота"
trainings['Максимальная высота'] = trainings['Максимальная высота'].str.replace(',', '')

# Теперь можно изменить тип данных в этой колонке на int и применить фильтрацию
trainings["Максимальная высота"] = trainings["Максимальная высота"].astype(int)
print(trainings[trainings["Максимальная высота"] > 600].head())
