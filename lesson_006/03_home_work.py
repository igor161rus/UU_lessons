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

    def horse_powers(self):
        self.hp = 100
        return self.hp


class Nissan(Car, Vehicle):
    price = 1000000
    vehicle_type = 'gibrid'

    def horse_powers(self):
        self.hp = 105
        return self.hp


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
print(car.horse_powers())
print(car.horse_powers)
# Вызвали функию horse_powers(), она из Nissan:
# bound method Nissan.horse_powers of <__main__.Nissan object at 0x0000027D7DCDAFD0>
print(car.__dict__)
# В пространстве имен car появилось значение 'hp': 105
# {'price': 10, 'hp': 105}
print(Nissan.__dict__)
# Но в пр-ве Nissan собственного hp нет, функция horse_powers этого класса его переопределяет, но для Nissan она
# нигде не вызывается


# Консоль:
# init Car <class '__main__.Nissan'>
# gibrid
# 1000000
# {}
# {'price': 10}
# {'__module__': '__main__', 'price': 1000000, 'vehicle_type': 'gibrid', 'horse_powers': <function Nissan.horse_powers at 0x0000027D7DCCC8B0>, '__doc__': None}
# {'__module__': '__main__', 'price': 2000000, 'hp': 0, '__init__': <function Car.__init__ at 0x0000027D7DCCC790>, 'horse_powers': <function Car.horse_powers at 0x0000027D7DCCC820>, '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None}
# {'__module__': '__main__', 'vehicle_type': 'none', 'price': 2, '__init__': <function Vehicle.__init__ at 0x0000027D7DCCC700>, '__dict__': <attribute '__dict__' of 'Vehicle' objects>, '__weakref__': <attribute '__weakref__' of 'Vehicle' objects>, '__doc__': None}
# 105
# <bound method Nissan.horse_powers of <__main__.Nissan object at 0x0000027D7DCDAFD0>>
# {'price': 10, 'hp': 105}
# {'__module__': '__main__', 'price': 1000000, 'vehicle_type': 'gibrid', 'horse_powers': <function Nissan.horse_powers at 0x0000027D7DCCC8B0>, '__doc__': None}
