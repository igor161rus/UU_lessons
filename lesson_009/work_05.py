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
