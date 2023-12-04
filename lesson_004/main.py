"""Беседа модулей"""

from module import function_1, function_2

print('Я ' + __file__.split('\\')[-1] + '. Я тут главный, я ' + __name__ + '\n')

if __name__ == '__main__':
    function_1()
    function_2()

# Результат
# D:\Python\Python39\python.exe D:\Python\Projects\UU\lessons\lesson_004\main.py
# Я module.py, сейчас я не main, меня вызвали
#
# Я main.py. Я тут главный, я __main__
#
# Йа function_1 нахожусь в модуле: module
# Функция function_1 модуля module. Печатает Hello, world
# Hello, world
#
# А я function_2 нахожусь в модуле: module
# Функция function_2 модуля module. Печатает Hello, world
# Hello, world
