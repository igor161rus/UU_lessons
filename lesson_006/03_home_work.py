# Ваша задача:
# Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers,
# которая возвращает количество лошидиных сил для автомобиля Создайте наследника класса Car и Vehicle - класс Nissan
# и переопределите свойство price и vehicle_type, а также переопределите функцию horse_powers
# Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price
# Получившийся код прикрепите к заданию текстом

class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000

    def __init__(self):
        self.hp = 0

    def horse_powers(self, hp):
        self.hp = hp
        return self.hp


class Nissan(Car, Vehicle):
    price = 1000000
    vehicle_type = 'gibrid'


car = Nissan()
print(car.vehicle_type)
print(car.price)