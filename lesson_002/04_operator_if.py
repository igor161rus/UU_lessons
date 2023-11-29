# 3
x = 38

print('привед!')
if x < 0:
    print('меньше нуля')
print('пока')

# Вывод
# D:\Python\Python39\python.exe D:\Python\Projects\UU\lesson_002\04_operator_if.py
# привед!
# пока


# 4
a, b = 10, 5

if a > b:
    print('a > b')

if a > b and a > 0:
    print('успех')

if (a > b) and (a > 0 or b < 1000):
    print('успех')

if 5 < b and b < 10:
    print('успех')
# Лучше так:
# if 5 < b < 10:
#     print('успех')

# Вывод
# D:\Python\Python39\python.exe D:\Python\Projects\UU\lesson_002\04_operator_if.py
# a > b
# успех
# успех


# 6
if '34' > '123':
    print('успех')

if '123' > '12':
    print('успех')

if [1, 2] > [1, 1]:
    print('успех')

# Вывод
# D:\Python\Python39\python.exe D:\Python\Projects\UU\lesson_002\04_operator_if.py
# успех
# успех
# успех


# 7
# нельзя сравнивать
if '6' > 5:
    print('успех')
# TypeError: '>' not supported between instances of 'str' and 'int'

if [5, 6] > 5:
    print('успех')
#TypeError: '>' not supported between instances of 'list' and 'int'

# можно
if '6' != 5:
    print('успех1')
