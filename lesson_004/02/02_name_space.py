def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


def test_function2():
    pass


func_list = [name for (name, obj) in vars().items()
             if hasattr(obj, "__class__") and obj.__class__.__name__ == "function"]
# lst_fn = []
# for (name, obj) in vars().items():
#     if hasattr(obj, "__class__") and obj.__class__.__name__ == "function":
#         lst_fn.append(name)
# print(lst_fn)

print(func_list)

try:
    inner_function()
except NameError:
    print('Нет такого объекта на этом уровне')
    print('Объявлены только: ')
    for i, j in enumerate(func_list):
        print(j)


# if 'inner_function' in globals():
#     print('Нет такого объекта на этом уровне')
# else:
#     test_function()
