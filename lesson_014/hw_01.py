# Создайте класс SuperDate, наследованный от класса datetime модуля datetime,
# объекты которого будут дополнительно обладать следующими методами:
#
# 1. get_season - должен возвращать сезон года (Summer, Autumn, Winter, Spring)
# 2. get_time_of_day - должен возвращать  время суток
# (Morning: 6-12; Day: 12-18, Evening: 18-0, Night: 0-6) (последнее число не включено в промежуток)
#
#
# Пример работы класса:
#
# a = SuperDate(2024, 2, 22, 12)
# print(a.get_season())
# print(a.get_time_of_day())
#
# Вывод на консоль:
# Winter
# Day
#
# Примечание:
# Для удобного хранения промежутков времени и номеров месяцев можно использовать словари.

from datetime import datetime


class SuperDate(datetime):
    def get_season(self):
        """Функция возвращает сезон года (Summer, Autumn, Winter, Spring)"""
        season = {
            1: 'Winter',
            2: 'Winter',
            3: 'Spring',
            4: 'Spring',
            5: 'Spring',
            6: 'Summer',
            7: 'Summer',
            8: 'Summer',
            9: 'Autumn',
            10: 'Autumn',
            11: 'Autumn',
            12: 'Winter'
        }
        return season[self.month]

    def get_time_of_day(self):
        """Функция возвращает время суток"""

        time_of_day = ['Night', 'Morning', 'Day', 'Evening']
        # if self.hour < 6:
        #     time_of_day = time_of_day[0]
        # elif self.hour < 12:
        #     time_of_day = time_of_day[1]
        # elif self.hour < 18:
        #     time_of_day = time_of_day[2]
        # else:
        #     time_of_day = time_of_day[3]
        return time_of_day[(int(self.hour)) // 6]


a = SuperDate(2024, 3, 11, 13)
# print(a.hour)
print(a.get_season())
print(a.get_time_of_day())

# Результат:
# E:\python\Python312\python.exe E:\python\projects\UU_lessons\lesson_014\hw_01.py
# Spring
# Day
#
# Process finished with exit code 0