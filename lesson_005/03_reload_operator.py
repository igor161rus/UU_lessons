class Buiding:
    def __init__(self, floors=0, b_type=''):
        self.numberOfFloors = floors
        self.buildingType = b_type

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


my_building1 = Buiding(10, 'десять')
my_building2 = Buiding(5, 'пять')

print('my_building1 = my_building1', my_building1 == my_building1)
print('my_building1 = my_building2', my_building1 == my_building2)
print('my_building2 = my_building1', my_building2 == my_building1)