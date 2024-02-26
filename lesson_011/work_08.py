from pprint import pprint

import requests

some_string = 'i am a string'
some_number = 42
some_list = [some_string, some_number]


def some_function(param, param_2='n/a'):
    print('my params is', param, param_2)


class SomeClass:
    def __init__(self):
        self.attribute_1 = 27

    def some_class_method(self, value):
        self.attribute_1 = value
        print(self.attribute_1)


some_object = SomeClass()

func = some_function

print(func.__name__)
# print(some_function.__name__)
print(SomeClass.__name__)
rq = requests
# print(some_object.__name__) # AttributeError: 'SomeClass' object has no attribute '__name__'
print(rq.__name__)
# print(requests.__name__)

print('*' * 10, '\n')
print(type(some_object))

print(type(some_number) is int)
print(type(some_number) is list)


def check_param(value):
    if type(value) is str:
        print('Обрабатываем строку', value)
    else:
        print('Это не строка')


check_param(value=some_string)
check_param(value=some_list)

print('*' * 10, '\n')
print(type(requests))

print('*' * 10, '\n')
# pprint(dir(some_number))
# pprint(dir(some_list))
# pprint(dir(some_function))
# pprint(dir(SomeClass))
# pprint(dir(some_object))
# pprint(dir())
#
# pprint(dir(requests))

print('*' * 10, 'hasattr \n')
attr_name = 'attribute_2'
print(hasattr(some_object, attr_name))

# print(getattr(some_object, attr_name)) # AttributeError: 'SomeClass' object has no attribute 'attribute_2'
print(getattr(some_object, attr_name, 'нет такого атрибута'))

print(hasattr(requests, 'get'))
http_get = getattr(requests, 'get')
print(type(http_get))

for attr_name in dir(requests):
    attr = getattr(requests, attr_name)
    print(attr_name, type(attr))

print('*' * 10, '\n')
print(hasattr(some_object, 'attribute_1'))
print(hasattr(some_object, 'attribute_2'))

print(getattr(some_object, 'attribute_1'))
print(some_object.attribute_1)
print(getattr(some_object, 'attribute_2', 'значение, если атрибута нет'))
print(getattr(some_object, attr_name, None))

print('*' * 10, '\n')
