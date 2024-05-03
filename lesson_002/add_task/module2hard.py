from random import randint

a = randint(3, 20)


def multiple_pair(a):
    print(a)
    pair = ''
    b = 0
    for i in range(0, a):
        for j in range(1, a):
            if j < i:
                b = i + j
                if a % b == 0:
                    print(j, ' ', i)
                    pair = str(j) + str(i) + pair
    return pair


print(multiple_pair(a))
