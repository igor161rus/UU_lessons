def function_1():
    """Функция function_1 модуля module. Печатает Hello, world"""
    print('Йа ' + function_1.__name__ + ' нахожусь в модуле: ' + __name__)
    print(function_1.__doc__)
    print('Hello, world\n')


def function_2():
    """Функция function_2 модуля module. Печатает Hello, world"""
    print('А я ' + function_2.__name__ + ' нахожусь в модуле: ' + __name__)
    print(function_2.__doc__)
    print('Hello, world')


if __name__ == '__main__':
    print('Я ' + __file__.split('\\')[-1] + '. Сейчас я main и работаю сам по себе\n')
    function_1()
    function_2()
else:
    print('Я ' + __file__.split('\\')[-1] + ', сейчас я не main, меня вызвали\n')


# Результат
# D:\Python\Python39\python.exe D:\Python\Projects\UU\lessons\lesson_004\module.py
# Я module.py. Сейчас я main и работаю сам по себе
#
# Йа function_1 нахожусь в модуле: __main__
# Функция function_1 модуля module. Печатает Hello, world
# Hello, world
#
# А я function_2 нахожусь в модуле: __main__
# Функция function_2 модуля module. Печатает Hello, world
# Hello, world
