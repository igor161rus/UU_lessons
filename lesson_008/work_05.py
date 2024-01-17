import warnings


def greet_person(person_name):
    if person_name == 'Robert':
        warnings.warn("We don't like you, Robert")
    print(f'Hi there {person_name}')


#warnings.simplefilter('ignore')
warnings.simplefilter('error')

try:
    greet_person('Robert')
    print('Выполнение продолжается')
except UserWarning:
    print('Warning')
for i in range(10):
    print(f'i={i}')
