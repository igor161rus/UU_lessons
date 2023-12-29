# Ваша задача:
# Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers,
# которая возвращает количество лошидиных сил для автомобиля Создайте наследника класса Car и Vehicle - класс Nissan
# и переопределите свойство price и vehicle_type, а также переопределите функцию horse_powers
# Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price
# Получившийся код прикрепите к заданию текстом

class Vehicle:
    vehicle_type = "none"
    price = 2

    def __init__(self):
        print(f'init Vehicle {self.__class__}')


class Car:
    price = 2000000
    hp = 0

    def __init__(self):
        print(f'init Car {self.__class__}')

    #        self.hp = 0

    def horse_powers(self, hp):
        self.hp = hp
        return self.hp


class Nissan(Car, Vehicle):
    price = 1000000
    vehicle_type = 'gibrid'


# Примечания для меня, что я понял
car = Nissan()
# Вызвался метод __init__ при создании экземляра класса Nissan
# init Car <class '__main__.Nissan'>
# зависит от порядка наследования Nissan(Car, Vehicle)
print(car.vehicle_type)
# gibrid
# Атрибут vehicle_type переопределен из базового класса Vehicle, в пространстве имен Nissan появилось значение 'gibrid'
# В базовом классе Vehicle vehicle_type = "none", там оно таким и осталось
print(car.price)
# Тоже самое с price, только этот атрибут взят из Car
print(car.__dict__)
# У объекта car нет в его пространстве имен собственных значений, все из базовых классов: {}
car.price = 10
# А вот теперь должно появится его собственное price
print(car.__dict__)
# Появилось: {'price': 10}
print(Nissan.__dict__)
# Видно, что в пространстве имен Nissan 'price': 1000000, 'vehicle_type': 'gibrid'
print(Car.__dict__)
# Пространство имен Car 'price': 2000000, 'hp': 0
print(Vehicle.__dict__)
# Пространство имен Vehicle: 'vehicle_type': 'none', 'price': 2
