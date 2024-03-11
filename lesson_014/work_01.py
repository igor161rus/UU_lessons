print((4.31 == 4.309999999999))
print(4.31.hex())
print(4.30999999999999.hex())
print(0.3 + 0.3 + 0.3 + 0.1)
print(round(0.3 + 0.3 + 0.3 + 0.1, 10))

from decimal import *

print(Decimal('0.3') + Decimal('0.3') + Decimal('0.3') + Decimal('0.1'))
getcontext().prec = 50

Andys_money_float = []
Andys_money_decimal = []

with open('external_data/Andys_goods.txt', 'r') as Andys_money:
    for line in Andys_money:
        Andys_money_float.append(float(line))
        Andys_money_decimal.append(Decimal(line))
exchange_rate = 1.2063
tax_rate = 0.13


def tax_calculation(income_in_dollars, exchange_rate, tax_rate):
    return tax_rate * sum(money * exchange_rate for money in income_in_dollars)


prfit_tax_amount = tax_calculation(Andys_money_float, exchange_rate, tax_rate)
print(f'float {prfit_tax_amount}')
prfit_tax_amount = tax_calculation(Andys_money_decimal, Decimal(exchange_rate), Decimal(tax_rate))
print(f'decimal {prfit_tax_amount}')
print('*' * 20, '\n')

# 2
Andys_money_float = []
Andys_money_decimal = []
with open('external_data/Andys_goods.txt', 'r') as Andys_money:
    for line in Andys_money:
        Andys_money_float.append(float(line))
        Andys_money_decimal.append(Decimal(line))

print(f'Цены в магазинах могут выглядеть так: {Andys_money_float[:5]}')
round_list = []
for price in Andys_money_float:
    round_list.append(round(price, 2))
revenue = sum(round_list)
print(f'Но даже если цены выглядят ровно {round_list[:5]}')
print(f'Могут возникать странные остатки при их суммировании {revenue}')

decimal_round_list = []
for price in Andys_money_decimal:
    decimal_round_list.append(price.quantize(Decimal('1.00')))
decimal_revenue = sum(decimal_round_list)
print(f'Получаем округленные цены{decimal_round_list[:5]}')
print(f'Считаем дневную выручку {decimal_revenue}')
print(f'Равны ли значения? Ответ - {decimal_revenue == revenue}')
print('*' * 20, '\n')


# 3
def mullers_formula(z, y):
    return 108 - (815 - 1500 / z) / y


# Сперва с помощью типа 'float'
float0 = 4.0
float1 = 4.25
# При таких начальных условмях, ряд должен сходиться к 5,
# проверим это, вычислив 30-й член ряда
for _ in range(2, 31):
    float2 = mullers_formula(float0, float1)
    float0, float1 = float1, float2
print(f'(float) 30-й член последовательности равен {float2}')

# А теперь попробуем использовать Decimal
getcontext().prec = 35
dec0 = Decimal(4.0)
dec1 = Decimal(4.25)
for _ in range(2, 31):
    dec2 = mullers_formula(dec0, dec1)
    dec0, dec1 = dec1, dec2
print(f'(Decimal) 30-й член последовательности равен {dec2}')

getcontext().prec = 50
dec0_50 = Decimal(4.0)
dec1_50 = Decimal(4.25)
for _ in range(2, 31):
    dec2_50 = mullers_formula(dec0_50, dec1_50)
    dec0_50, dec1_50 = dec1_50, dec2_50
print(f'Теперь 30-й член последовательности равен {dec2_50}')
print(f'Разница между первым и вторым вычислениями составила {dec2 - dec2_50}')
print('*' * 20, '\n')

# 4
number = Decimal('10.025')
print(f'Банковский метод - {number.quantize(Decimal("1.00"), ROUND_HALF_EVEN)}')
print(f'Арифметический метод - {number.quantize(Decimal("1.00"), ROUND_HALF_UP)}')
print(f'Метод обрезания чисел без округления - {number.quantize(Decimal("1.00"), ROUND_FLOOR)}')