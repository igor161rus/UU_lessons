from random import randint

a = randint(3, 20)

print(str(a) + ' - число из первой вставки')
pair = ''
b = 0
for i in range(1, a):
    for j in range(1, a):
        if j > i:
            b = i + j
            if a % b == 0:
                pair = pair + str(i) + str(j)

print(pair + ' - нужный пароль')
