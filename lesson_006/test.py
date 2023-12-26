class Pet:
    legs = 4
    has_teil = True

    def __init__(self, name):
        self.name = name

    def inspect(self):
        print(self.__class__.__name__, self.name)
        print(('Всего ног: '), self.legs)
        print('Хвост присутствует -', 'да' if self.has_teil else 'нет')
        print(self.__dict__)


class Cat(Pet):
    def sound(self):
        print('Мяу')


class Bobtail(Cat):
    has_teil = False


pet = Pet(name='Невиданное чудо')
pet.legs = 5
pet.inspect()
print(pet.__class__ is Pet)

my_pet = Bobtail('Bob')
my_pet.inspect()
my_pet.sound()
