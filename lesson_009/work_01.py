# def by_3(x):
#     return x * 3
#
#
# def is_odd(x):
#     return x % 2
#
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# result = map(by_3, filter(is_odd, my_numbers))
# print(list(result))


# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# result = map(lambda x: x * 3, filter(lambda x: x % 2, my_numbers))
# print(list(result))

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
print(my_numbers)
print(they_numbers)
print()
result = [x * 3 for x in my_numbers]
print(list(result))

result = [x for x in my_numbers if x % 2]
print(result)

result = [x * 3 for x in my_numbers if x % 2]
print(result)
print()

result = [x * y for x in my_numbers for y in they_numbers]
print(result)
result = [x * y for x in my_numbers for y in they_numbers if x % 2]
print(result)
result = [x * y for x in my_numbers for y in they_numbers if x % 2 and y // 2]
print(result)
print()

result = {x for x in my_numbers}
print(result, type(result))
print()

result = {x: x ** 2 for x in my_numbers}
print(result, type(result))
print()

result = (x ** 10000 for x in my_numbers)
print(result)
for elem in result:
    print(elem)
print('Еще раз')
for elem in result:
    print(elem)

result = (x ** 300000 for x in my_numbers)
for i in result:
    print(i)
    if str(i).startswith('100'):
        break
