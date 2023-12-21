import math


class House:
    """
    Класс House принимает на входе 4 параметра:
    number_of_floors - количество этажей
    number_of_apart_floor - количество квартир на этаже
    start_apart - этаж с котого начинаются квартиры
    entrance - количество подъездов

    Другие атрибуты
    apart - список всех квартир
    ap_fl - список квартир по этажам. Зачем так сделал - хотел повозиться с генераторами
    mode - режим ответов: 1 - нормальный, 2 - злая бабуся
    start_apart - с какого этажа начинаются квартиры
    entrance_count - количество подъездов
    entrance_select - выбранный подъезд

    Методы:
    list_apart - выводит поэтажный список квартир
    get_apart - выводит этаж на котором находится квартира
    get_entrance - Функция выбора подъезда
    setNewNumberOfFloors - Функция для 2го домашнего задания
    calc_apart - Функция заполнения списка квартир
    house_menu - меню
    """

    def __init__(self, floors, aparts_floor, start_apart, entrance):
        self.number_of_floors = floors
        self.number_of_apart_floor = aparts_floor
        self.mode = 0
        self.start_apart = start_apart
        self.entrance_count = entrance
        self.entrance_select = 1
        self.apart = []
        self.ap_fl = []
        self.calc_apart()
        print(f'Вумный коньсерж Вас приветствует!\n'
              f'В нашем доме {self.entrance_count} подъездов по {self.number_of_floors} этажей\n'
              f'{(self.number_of_floors - 1) * self.number_of_apart_floor * self.entrance_count} квартир\n'
              f'Вы находитесь в {self.entrance_select} подъезде\n'
              f'В нашем подъезде:\n {len(self.apart)} квартир\n'
              f'Квартиры начинаются с {self.start_apart} этажа\n')

    def list_apart(self):
        """Функция вывода поэтажного списка квартир"""
        for i in range(len(self.ap_fl)):
            print(f'Этаж {i + self.start_apart}: квартиры')
            for j in range(len(self.ap_fl[i])):
                print(self.ap_fl[i][j], end=' ')
            print()

    def get_apart(self):
        """Функция для определения этажа по номеру квартиры"""
        my_ap = int(input('В какую квартиру желаете попасть? '))
        if my_ap in self.apart:
            print(f'Вам на '
                  f'{math.ceil(my_ap / self.number_of_apart_floor / self.entrance_select) + self.start_apart - 1} '
                  f'этаж\n')
        else:
            # Культурный режим
            if self.mode == 0:
                print('Не туда попали, нет такой квартиры')
            # Режим злой бабуси
            else:
                print('Куды прешь, нету такой квартиры. Топчут тут...')

    def get_entrance(self):
        """Функция выбора подъезда"""
        self.entrance_select = int(input('Введите номер подъезда '))
        self.calc_apart()

    def setNewNumberOfFloors(self, floors):
        """Функция для 2го домашнего задания"""
        self.number_of_floors = floors
        print(self.number_of_floors)
        self.calc_apart()

    def calc_apart(self):
        """Функция заполнения списка квартир"""
        start_range = ((self.number_of_floors - self.start_apart + 1) * self.number_of_apart_floor *
                       (self.entrance_select - 1) + 1)
        end_range = (self.number_of_floors - self.start_apart + 1) * self.number_of_apart_floor + start_range
        self.apart = [i for i in range(start_range, end_range)]
        self.ap_fl = [self.apart[i:i + self.number_of_apart_floor] for i in
                      range(0, len(self.apart), self.number_of_apart_floor)]

    def house_menu(self):
        """Функция обработки меню"""
        dict_menu = {0: 'Подъезд', 1: 'Список квартир', 2: 'Ищу квартиру', 3: 'Справка', 4: 'Выполнить задание урока 1',
                     5: 'Выполнить задание урока 2', 6: 'Переключить режим', 7: 'Выход'}
        print('Выберите пункт меню:')
        for i in dict_menu:
            print(f'{i}: {dict_menu[i]}')
        sel_menu = int(input('_'))
        if sel_menu == 0:
            self.get_entrance()
            return True
        elif sel_menu == 1:
            self.list_apart()
            return True
        elif sel_menu == 2:
            self.get_apart()
            return True
        elif sel_menu == 3:
            print(self.__doc__)
            return True
        elif sel_menu == 4:
            for i in range(1, self.number_of_floors + 1):
                print(f'Текущий этаж равен: {i}')
            return True
        elif sel_menu == 5:
            floors = int(input('_'))
            self.setNewNumberOfFloors(floors)
            return True
        elif sel_menu == 6:
            if self.mode == 0:
                self.mode = 1
                print('Режим злой бабуси включен')
                return True
            else:
                self.mode = 0
                print('Нормальный режим включен')
                return True
        elif sel_menu == 7:
            if self.mode == 0:
                print('Хорошего дня! До встречи!')
            else:
                print('Иди иди! И показания по воде чтоб сдали!')
            return False


my_house = House(15, 4, 2, 8)
loop = True
while loop:
    loop = my_house.house_menu()

# Результат:
# C:\Users\admin\AppData\Local\Programs\Python\Python311\python.exe E:\python\projects\UU_lessons\lesson_005\attributes_methods.py
# Вумный коньсерж Вас приветствует!
# В нашем доме 8 подъездов по 15 этажей
# 448 квартир
# Вы находитесь в 1 подъезде
# В нашем подъезде:
#  56 квартир
# Квартиры начинаются с 2 этажа
#
# Выберите пункт меню:
# 0: Подъезд
# 1: Список квартир
# 2: Ищу квартиру
# 3: Справка
# 4: Выполнить задание урока 1
# 5: Выполнить задание урока 2
# 6: Переключить режим
# 7: Выход

# Домашняя работа по уроку "Атрибуты и методы объекта."
# _4
# Текущий этаж равен: 1
# Текущий этаж равен: 2
# Текущий этаж равен: 3
# Текущий этаж равен: 4
# Текущий этаж равен: 5
# Текущий этаж равен: 6
# Текущий этаж равен: 7
# Текущий этаж равен: 8
# Текущий этаж равен: 9
# Текущий этаж равен: 10
# Текущий этаж равен: 11
# Текущий этаж равен: 12
# Текущий этаж равен: 13
# Текущий этаж равен: 14
# Текущий этаж равен: 15

# Выберите пункт меню:
# 0: Подъезд
# 1: Список квартир
# 2: Ищу квартиру
# 3: Справка
# 4: Выполнить задание урока 1
# 5: Выполнить задание урока 2
# 6: Переключить режим
# 7: Выход

# Домашняя работа по уроку "Специальные методы классов"
# _5
# _8
# 8
