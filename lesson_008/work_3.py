# def greet_person(person_name):
#     if person_name == 'Robert':
#         raise BaseException("We don't like you, Robert")
#     print(f'Hi there {person_name}')
#
#
# greet_person('Dolly')
# greet_person('Robert')

# try:
#     raise NameError('Привет Там')
# except NameError as exc:
#     print(f'Исключение типа {type(exc)} пролетело мимо! Его параметры {exc.args}')
#     raise

# try:
#     raise NameError('Привет там')
# except NameError as exc:
#     print(f'Исключение типа {type(exc)}')
#     raise TypeError('Привет и тут')

class HeroDiedError(Exception):
    pass


class GameOverError(Exception):
    pass


try:
    raise HeroDiedError('Рядовой Райан')
except HeroDiedError as exc:
    print(f'Поймано исключение {exc}')
    raise GameOverError('Миссия провалена')
