import logging


def perky(param):
    return param / 0


logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.FileHandler('error.log', 'w', 'utf-8')]
)

number = 42
try:
    logging.info('Посмотрим как у него получится...')
    perky(number)
    logging.info('Он смог!')
except Exception:
    logging.exception(f'Дерзкий не справился с {number}')
