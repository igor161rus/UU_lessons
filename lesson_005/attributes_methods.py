import math


class House(object):
    """
    number_of_floors - количество этажей
    number_of_apart_floor - количество квартир на этаже
    apart - список всех квартир
    ap_fl - список квартир по этажам
    """

    def __init__(self, floors, aparts_floor):
        self.number_of_floors = floors
        self.number_of_apart_floor = aparts_floor
        self.apart = [i for i in range(1, self.number_of_floors * self.number_of_apart_floor + 1)]
        self.ap_fl = [self.apart[i:i + self.number_of_apart_floor] for i in
                      range(0, len(self.apart), self.number_of_apart_floor)]
        print(f'Вумный коньсерж Вас приветствует!\nВ нашем подъезде:\n {len(self.apart)} квартир\n '
              f'{self.number_of_floors} этажей\n')

    def list_apart(self):
        for i in range(len(self.ap_fl)):
            print(f'Этаж {i + 1}: квартиры')
            for j in range(len(self.ap_fl[i])):
                print(self.ap_fl[i][j], end=' ')
            print()

    def get_apart(self):
        my_ap = int(input('В какую квартиру желаете попасть? '))
        if len(my_house.apart) >= my_ap > 0:
            print(f'Вам на {math.ceil(my_ap / 4)} этаж')
        else:
            print('Не туда попали, нет такой квартиры')

    def house_menu(self):
        dict_menu = {1: 'Список квартир', 2: 'Ищу квартиру', 3: 'Справка', 4: 'Выход'}
        print('Выберите пункт меню:')
        sel_menu = int(input('_'))
        for i in dict_menu:
            print(f'{i}: {dict_menu[i]}')
        if sel_menu == 1:
            self.list_apart()
        elif sel_menu == 2:
            self.get_apart()
        elif sel_menu == 3:
            print(self.__doc__)
        elif sel_menu == 4:
            return False


my_house = House(10, 4)
while True:
    my_house.house_menu()
