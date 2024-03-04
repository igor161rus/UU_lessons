import logging

from primes_package.work_08_01_primes import prime_numbers_generator

main_log = logging.getLogger('main')

def print_primes(n):
    for prime in prime_numbers_generator(n):
        main_log.info(f'Простое из генераторов {prime}')

if __name__ == '__main__':
    print_primes(n=10)