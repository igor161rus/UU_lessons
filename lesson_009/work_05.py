def fibonacchi_v2(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


fib = fibonacchi_v2(n=10)
print(fib)
for value in fib:
    print(value)
