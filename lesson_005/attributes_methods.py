import math


class House:
    """
    Класс House принимает на входе два параметра:
    number_of_floors - количество этажей
    number_of_apart_floor - количество квартир на этаже

    Друшие атрибуты
    apart - список всех квартир
    ap_fl - список квартир по этажам. Зачем так сделал - хотел повозиться с генераторами
    mode - режим ответов: 1 - нормальный, 2 - злая бабуся
    start_apart - с какого этажа начинаются квартиры
    entrance_count - количество подъездов
    entrance_select - выбранный подъезд

    Методы:
    list_apart - выводит поэтажный список квартир
    get_apart - выводит этаж на котором находится квартира
    house_menu - меню
    """

    def __init__(self, floors, aparts_floor, start_apart, entrance):
        self.number_of_floors = floors
        self.number_of_apart_floor = aparts_floor
        self.mode = 0
        self.start_apart = start_apart
        self.entrance_count = entrance
        self.entrance_select = 1
        # self.apart = [i for i in range(self.entrance_select, (self.number_of_floors - self.start_apart + 1)
        #                                * self.number_of_apart_floor + 1)]
        # self.ap_fl = [self.apart[i:i + self.number_of_apart_floor] for i in
        #               range(0, len(self.apart), self.number_of_apart_floor)]
        self.apart = []
        self.ap_fl = []
        self.calc_apart()
        print(self.apart)
        print(self.ap_fl)
        print(f'Вумный коньсерж Вас приветствует!\n'
              f'В нашем доме {self.entrance_count} подъездов по {self.number_of_floors} этажей\n'
              f'Вы находитесь в {self.entrance_select} подъезде\n'
              f'В нашем подъезде:\n {len(self.apart)} квартир\n'
              f'Квартиры начинаются с {self.start_apart} этажа\n')

    def list_apart(self):
        print(self.apart)
        print(self.ap_fl)
        for i in range(len(self.ap_fl)):
            print(f'Этаж {i + self.start_apart}: квартиры')
            for j in range(len(self.ap_fl[i])):
                print(self.ap_fl[i][j], end=' ')
            print()

    def get_apart(self):
        print(self.apart)
        print(self.ap_fl)
        my_ap = int(input('В какую квартиру желаете попасть? '))
        if my_ap in self.apart:
            print(f'Вам на {math.ceil(my_ap / self.number_of_apart_floor / self.entrance_select) + self.start_apart - 1} этаж')
        else:
            # Культурный режим
            if self.mode == 0:
                print('Не туда попали, нет такой квартиры')
            # Режим злой бабуси
            else:
                print('Куды прешь, нету такой квартиры. Топчут тут...')

    def get_entrance(self):
        self.entrance_select = int(input())
        self.calc_apart()

    def setNewNumberOfFloors(self, floors):
        self.number_of_floors = floors
        print(self.number_of_floors)
        self.calc_apart()

    def calc_apart(self):
        start_range = self.number_of_floors * self.number_of_apart_floor * (self.entrance_select - 1) + 1
        end_range = (self.number_of_floors - self.start_apart + 1) * self.number_of_apart_floor + 1
        self.apart = [i for i in range(start_range, end_range)]
        print(f'calc_apart {self.apart}')
        self.ap_fl = [self.apart[i:i + self.number_of_apart_floor] for i in
                      range(0, len(self.apart), self.number_of_apart_floor)]

    def house_menu(self):
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
# D:\Python\Python39\python.exe D:\Python\Projects\UU\lessons\lesson_005\attributes_methods.py
# Вумный коньсерж Вас приветствует!
# В нашем подъезде:
#  40 квартир
#  10 этажей
#
# Выберите пункт меню:
# 1: Список квартир
# 2: Ищу квартиру
# 3: Справка
# 4: Выполнить задание урока
# 5: Переключить режим
# 6: Выход
# _
#
# _1
# Этаж 1: квартиры
# 1 2 3 4
# Этаж 2: квартиры
# 5 6 7 8
# ...
# ...
# Этаж 9: квартиры
# 33 34 35 36
# Этаж 10: квартиры
# 37 38 39 40

# _2
# В какую квартиру желаете попасть? 23
# Вам на 6 этаж
#
# _2
# В какую квартиру желаете попасть? 100
# Не туда попали, нет такой квартиры

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

# _5
# Режим злой бабуси включен
# _2
# В какую квартиру желаете попасть? 100
# Куды прешь, нету такой квартиры. Топчут тут...
