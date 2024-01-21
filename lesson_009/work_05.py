def fibonacchi_v2(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


fib = fibonacchi_v2(n=10)
print(fib)
for value in fib:
    print(value)
print()
print('****************************************')
print()


def fibonacci_v3():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for value in fibonacci_v3():
    print(value)
    if value > 10 ** 6:
        break

print(121393 in fibonacci_v3())
print()
print('****************************************')
print()


def fibinacci_v4():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        if a > 10 ** 30:
            return


for val in fibinacci_v4():
    print(val)
print()
print('****************************************')
print()

list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

for x in list_1:
    for y in list_2:
        result = x * y
        print(x, y, result)
        if result == to_find:
            print('Found!!!')
            can_continue = False
            break
    if not can_continue:
        break


def get_next_result(list_1, list_2):
    for x in list_1:
        for y in list_2:
            yield x, y, x * y


for x, y, result in get_next_result(list_1, list_2):
    if result == to_find:
        print('Found!!!')
        can_continue = False
        break
print()
print('****************************************')
print()


def queue(*args):
    data = list(args)
    while data:
        next = data.pop(0)
        new_value = (yield next)
        if new_value is not None:
            data.append(new_value)


shop_queue = queue('Вася', 'Марина', 'Владислав', 'Эльвира')
for name in shop_queue:
    print(f'К кассе приглашается {name}')
    if name == 'Марина':
        print('А кто последний?')
        name = shop_queue.send('Маргарита Ивановна')
        print(f'К кассе приглашается {name}')
