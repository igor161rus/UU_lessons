def get_name_area_function(area):
    """Функция выводящая список объявленных функций в вызываемой области. Списковые включения"""
    list_function = [name for (name, obj) in area
                     if hasattr(obj, "__class__") and obj.__class__.__name__ == "function"]
    print('\nВ этой области определены:')
    for i, j in enumerate(list_function):
        print(f'{i + 1} {j}')
#    return list_function


def test_function():
    """Тестовая функция в глобальной области"""
    def inner_function():
        """Локальная функция в test_function"""
        print(f'Я функция inner_function, я в области видимости функции test_function\n{inner_function.__doc__}')

    inner_function()

    def inner_function_2():
        """Локальная функция 2 в test_function"""
        pass

    get_name_area_function(vars().items())


def test_function2():
    """Тестовая функция 2 в глобальной области"""
    pass


try:
    print('\nПопытка вызова функции inner_function')
    inner_function()
except NameError:
    print('Нет такого объекта на этом уровне')
    get_name_area_function(globals().items())
    # for i, j in enumerate(get_name_area_function(globals().items())):
    #     print(f'{i + 1} {j}')
print(f'\nВызов функции test_function {test_function.__doc__}')
test_function()
# if 'inner_function' in globals():
#     print('Нет такого объекта на этом уровне')
# else:
#     test_function()


# Результат:
# C:\Users\Igor\AppData\Local\Programs\Python\Python311\python.exe C:\Python\Projects\UU_lessons\lesson_004\02\02_name_space.py
#
# Попытка вызова функции inner_function
# Нет такого объекта на этом уровне
#
# В этой области определены:
# 1 get_name_area_function
# 2 test_function
# 3 test_function2
#
# Вызов функции test_function Тестовая функция в глобальной области
# Я функция inner_function, я в области видимости функции test_function
# Локальная функция в test_function
#
# В этой области определены:
# 1 inner_function_2
# 2 inner_function
