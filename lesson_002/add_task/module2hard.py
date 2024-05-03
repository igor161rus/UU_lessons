from random import randint

a = randint(3, 20)

# 11 - 11029384756

a = 11

def multiple_pair(a):
    print(a)
    pair = ''
    b = 0
    for i in range(1, a):
        for j in range(1, a):
            if j > i:
                b = i + j
                if a % b == 0:
                    print(i, ' ', j)
                    pair = pair + str(i) + str(j)
    return pair


print(multiple_pair(a))
print('11029384756')
