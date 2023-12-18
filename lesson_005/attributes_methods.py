class House:
    number_of_floors = 10
    number_of_apart_floor = 4
    number_floor = 15

    def apart_on_floor(self):
        floor = 1
        aparts = []
        apart = 1
        while floor <= 10:
            # for j in range(1, self.number_of_apart_floor + 1):
            #     print(f'{floor} {j}')
            aparts = [[self.number_of_floors] for j in range(self.number_of_apart_floor)]
                # aparts[floor][j] = apart
                # apart += 1
            print(aparts)
            print(f'На {floor}')
            floor += 1


my_house = House()
# for i in range(1, my_house.number_of_floors + 1):
#     print('Текущий этаж равен: ' + str(i))
# my_house.apart_on_floor()
apart = [i for i in range(1, my_house.number_of_floors * my_house.number_of_apart_floor + 1)]
print(apart)

w, h = 5, 3  # зададим ширину и высотку матрицы
matrix = [[x for x in apart] for y in range(h)]
print(matrix)   # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]