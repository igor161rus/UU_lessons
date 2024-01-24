def func_decorator(func):
    def wrapper(*args, **kwargs):
        print('----- что-то делаем до вызова функции -----')
        res = func(*args, **kwargs)
        print('----- что-то делаем после вызова функции -----')
        return res

    return wrapper