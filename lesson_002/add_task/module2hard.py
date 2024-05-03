from random import randint

a = randint(3, 20)
def multiple_pair(a):
    print(a)
    b = 0
    for i in range(0, a):
        for j in range(1, a):
            if j < i:
                b = i + j
                if a % b == 0:
                    print(i, ' ', j)
    return b

print(multiple_pair(a))