my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
my_numbers.sort(key=lambda x: -x)
print(my_numbers)

my_numbers.sort(key=lambda x: -x if x >= 5 else x)
print(my_numbers)

they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]

my_pairs = list(zip(my_numbers, they_numbers))
print(my_pairs)

my_pairs = [(3, 2), (1, 7), (4, 1), (1, 8), (5, 2), (9, 8), (2, 1), (6, 8)]
print(my_pairs)
my_pairs.sort(key=lambda x: x[0])
print(my_pairs)

my_pairs.sort(key=lambda x: x[1])
print(my_pairs)