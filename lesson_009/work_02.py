def get_russian_names():
    return ['Ваня', 'Коля', 'Маша', ]


def get_british_names():
    return ['Oliver', 'Jack', 'Harry', ]


def print_names(message, name_getter):
    print(message, name_getter())


print(type(get_russian_names))
print(get_russian_names.__name__)
print()

my_func = get_russian_names
print(my_func())
print(my_func.__name__)
print()

name_getters = [get_russian_names, get_british_names]
for name_getter in name_getters:
    print(name_getter())
print()

print_names(message='Русские имена', name_getter=get_russian_names)
print()

names = {'Русские имена': get_russian_names, 'Английские имена': get_british_names}
for message, name_getter in names.items():
    print_names(message, name_getter)
print('*************************************')
print()


def adder(*args):
    res = 0
    for number in args:
        res += number
    return res


def multiplier(*args):
    res = 1
    for number in args:
        res *= number
    return res


def process_numbers(numbers, handler):
    result = handler(*numbers)
    print(f'Получилось {result}')


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
process_numbers(numbers=my_numbers, handler=adder)
process_numbers(numbers=my_numbers, handler=multiplier)
print('*************************************')
print()


def mul_by_2(x):
    return x * 2


def mul_by_3(x):
    return x * 3


result = map(mul_by_2, my_numbers)
print(result)
print(list(result))
result = map(mul_by_3, my_numbers)
print(list(result))
print('*************************************')
print()


def is_odd(x):
    return x % 2


result = filter(is_odd, my_numbers)
print(result)
print(list(result))
print()

result = map(mul_by_3, filter(is_odd, my_numbers))
print(list(result))
result = sum(map(mul_by_3, filter(is_odd, my_numbers)))
print(result)
