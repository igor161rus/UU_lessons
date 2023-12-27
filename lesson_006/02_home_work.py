# Ваша задача: Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию
# def horse_powers, которая возвращает количество лошидиных сил для автомобиля Создайте наследника класса Car - класс
# Nissan и переопределите свойство price, а также переопределите функцию horse_powers Дополнительно создайте класс
# Kia, который также будет наследником класса Car и переопределите также свойство price, а также переопределите
# функцию horse_powers Получившийся код прикрепите к заданию текстом

class Car:
    # price = 1000000
    # hp = 100

    def __init__(self):
        self.price = 1000000
        self.hp = None

    def horse_powers(self):
        self.hp = 100

    def __str__(self):
        return '{} {} {}'.format(self.__class__.__name__, self.price, self.horse_powers())


class Nissan(Car):
    def horse_powers(self):
        self.hp = 150


class Kia(Car):
    price = 1500000

    def horse_powers(self):
        hp = 180


my_car = Nissan()
print(my_car)
my_car.horse_powers()
print(my_car)
