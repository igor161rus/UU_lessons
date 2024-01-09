import math

print('{} форматирование {} строк'.format('красивое', 'длинных'))

a = 'красивое'
b = 'длинных'
print('{0} форматирование {1} строк'.format(a, b))

a = 27
print('Число {0}'.format(a))
print('Число {0:3d}'.format(a))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d} '.format(x, x**2, x**3))

print('Вывод числа "{0:5f}" '.format(math.pi))
print('Вывод числа "{0:5.2f}" '.format(math.pi))
print('Вывод числа "{0:10.5f}" '.format(math.pi))

print('Вывод числа "{pi:30}" '.format(pi=math.pi))
