class Building:
    total = 0

    def __init__(self):
        Building.total += 1
        # print(self.total)


buildings = []
for i in range(40):
    my_building = Building()
    buildings.append(my_building)
print(buildings)
