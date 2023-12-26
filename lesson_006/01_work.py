class Pet:
    legs = 4
    has_teil = True

    def inspect(self):
        print(('Всего ног: '), self.legs)
        print('Хвост присутствует -', 'да' if self.has_teil else 'нет')


class Cat(Pet):
    def sound(self):
        print('Мяу')


class Dog(Pet):
    def sound(self):
        print('Гав')


class Hamster(Pet):
    def sound(self):
        print('Цццццц')

print('Котик')
my_pet = Cat()
my_pet.inspect()
my_pet.sound()

print('Собачка')
my_pet = Dog()
my_pet.inspect()
my_pet.sound()

print('Хомячок')
my_pet = Hamster()
my_pet.inspect()
my_pet.sound()