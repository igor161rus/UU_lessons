import inspect
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

print(callable(some_string))
print(callable(some_function))
print(callable(some_object.attribute_1))
print(callable(some_object.some_class_method))
print('*' * 10, '\n')

for attr_name in dir(requests):
    attr = getattr(requests, attr_name)
    print(attr_name, type(attr), callable(attr))
print('*' * 10, '\n')

print(hasattr(requests, 'get'))
http_get = getattr(requests, 'get')
print(type(http_get))
print(callable(http_get))
print('*' * 10, '\n')

print(isinstance(some_number, str))
print(isinstance(some_number, int))
print(isinstance(some_number, SomeClass))
print(isinstance(some_object, SomeClass))
print('*' * 10, '\n')

response = requests.get(url='https://www.youtube.com')
print(response, type(response), callable(response))
print(isinstance(response, requests.Response))
print(isinstance(response, requests.NullHandler))
print('*' * 10, '\n')


class DerivedClass(SomeClass):
    pass


some_object_2 = DerivedClass()

print(issubclass(SomeClass, DerivedClass))
print(issubclass(DerivedClass, SomeClass)) #??
print(isinstance(some_object_2, SomeClass))
print(isinstance(some_object_2, DerivedClass))
print('*' * 10, '\n')

print(issubclass(requests.ConnectTimeout, requests.HTTPError))
print(issubclass(requests.ConnectTimeout, requests.RequestException))
print('*' * 10, '\n')

print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))
print(inspect.isbuiltin(requests))
print('*' * 10, '\n')

some_function_module = inspect.getmodule(some_function)
print(type(some_function_module), some_function_module)
print('*' * 10, '\n')

some_function_module = inspect.getmodule(requests.get)
print(type(some_function_module), some_function_module.__name__)
print('*' * 10, '\n')

signature = inspect.signature(some_function)
print(type(signature), signature)
print(dir(signature))
print(type(signature.parameters), signature.parameters)
for param_name, param in signature.parameters.items():
    print(type(param), param)
    print(dir(param))
print('*' * 10, '\n')
for param_name, param in signature.parameters.items():
    print(type(param), param, param.name, param.default)