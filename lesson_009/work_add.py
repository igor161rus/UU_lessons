def func_decorator(func):
    def wrapper(*args, **kwargs):
        print('----- что-то делаем до вызова функции -----')
        res = func(*args, **kwargs)
        print('----- что-то делаем после вызова функции -----')
        return res

    return wrapper


@func_decorator
def some_func(title, tag):
    print(f'title = {title}, tag = {tag}')
    return f'<{tag}>{title}</{tag}>'

some_func('Python навсегда', 'h1')
# some_func = func_decorator(some_func)
# res = some_func('Python навсегда', 'h1')
# print(res)