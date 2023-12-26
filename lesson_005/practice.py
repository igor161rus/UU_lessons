import os
from random import randint
from termcolor import cprint

os.system('color')


class Man:
    def __init__(self, name):
        self.name = name
        self.fulness = 50
        self.house = None

    def __str__(self):
        return 'я - {}, сытость {}'.format(self.name, self.fulness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fulness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='yellow')

    def work(self):
        cprint('{} ходил на работу'.format(self.name), color='red')
        self.house.money += 50
        self.fulness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV'.format(self.name), color='green')
        self.fulness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились'.format(self.name), color='magenta')

    def act(self):
        if self.fulness <= 0:
            cprint('{} ...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fulness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money <= 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()

    def go_to_house(self, house):
        self.house = house
        cprint('{}'.format(self.name), color='cyan')
        self.fulness -= 10


class House:
    def __init__(self):
        self.food = 10
        self.money = 50

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось - {}'.format(
            self.food, self.money)


citizens = [
    Man(name='Бэвис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]

my_sweet_home = House()
for citizen in citizens:
    citizen.go_to_house(house=my_sweet_home)

for day in range(1, 21):
    print('================ день {} ==============='.format(day))
    for citizen in citizens:
        citizen.act()
    print('----------------- в конце дня ----------')
    for citizen in citizens:
        print(citizen)

    print(my_sweet_home)

# print(vasya)
# vasya.eat()
# print(vasya)
# vasya.work()
# print(vasya)
# vasya.play_DOTA()
# print()
