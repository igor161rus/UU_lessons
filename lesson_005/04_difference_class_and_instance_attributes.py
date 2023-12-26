class Building:
    total = 0

    def __init__(self, n):
        Building.total += 1
        self.total = n

    def __str__(self):
        return "bulding_" + str(self.total)

    __repr__ = __str__


buildings = []
for i in range(40):
    my_building = Building(i)
    buildings.append(my_building)
print(buildings)

# for i in range(40):
#     my_building = Building()
#     print(my_building.total)
#     print(my_building)
