import logging


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        logging.debug(f'number {number}')
        for prime in prime_numbers:
            if number % prime == 0:
                logging.debug(f'делится на {prime}')
                break
        else:
            logging.debug(f'найдено новое простое {number}')
            prime_numbers.append(number)
            yield number


# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO)


logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.FileHandler('primes.log', 'w', 'utf-8')]
)

for prime in prime_numbers_generator(100):
    logging.info(f'Простое из генераторов {prime}')
