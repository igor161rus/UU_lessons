import logging

from lesson_012.work_02 import prime_numbers_generator

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.FileHandler('primes.log', 'w', 'utf-8')],
)

for prime in prime_numbers_generator(100):
    logging.info(f'Простое из генераторов {prime}')
