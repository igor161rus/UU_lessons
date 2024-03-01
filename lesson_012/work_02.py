def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        print(f'number {number}')
        for prime in prime_numbers:
            if number % prime == 0:
                print(f'делится на {prime}')
                break
        else:
            print(f'найдено новое простое {number}')
            prime_numbers.append(number)
            yield number


for prime in prime_numbers_generator(100):
    print(f'Простое из генераторов {prime}')
