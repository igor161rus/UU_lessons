# Ваша задача: Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию
# def horse_powers, которая возвращает количество лошидиных сил для автомобиля Создайте наследника класса Car - класс
# Nissan и переопределите свойство price, а также переопределите функцию horse_powers Дополнительно создайте класс
# Kia, который также будет наследником класса Car и переопределите также свойство price, а также переопределите
# функцию horse_powers Получившийся код прикрепите к заданию текстом

class Car:
    price = 0

    def __init__(self):
        self.hp = 0

    def horse_powers(self, hp):
        self.hp = hp
        return self.hp

    def set_price(self):
        pass

    def __str__(self):
        return 'авто {}, стоимость {}, {} л/с '.format(self.__class__.__name__, self.price, self.hp)


class Nissan(Car):
    price = self.price
    def horse_powers(self, hp):
        self.hp = hp
        power = hp // 1.35962
        return self.hp, power


class Kia(Car):
    def horse_powers(self, hp):
        self.hp = hp
        power = hp // 1.35962
        return self.hp, power


my_car = Nissan()
print(my_car)
my_car.price = 1500000
ret = my_car.horse_powers(160)
print('авто {}, {} л/с, {} квт'.format(my_car.__class__.__name__, ret[0], ret[1]))
print(my_car)

my_car2 = Kia()
print(my_car2)
my_car2.price = 1200000
ret = my_car2.horse_powers(105)
print('авто {}, {} л/с, {} квт'.format(my_car2.__class__.__name__, ret[0], ret[1]))
print(my_car2)
