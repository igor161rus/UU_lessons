import math
from functools import wraps


def df_decorator(dx=0.01):
    def func_decorator(func):
        @wraps(func)
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        # wrapper.__name__ = func.__name__
        # wrapper.__doc__ = func.__doc__
        return wrapper

    return func_decorator


@df_decorator(dx=0.001)
def sin_df(x):
    """Функция для вычесления производной синуса"""
    return math.sin(x)


# f = df_decorator(dx=0.001)
# sin_df = f(sin_df)
#
# sin_df = df_decorator(dx=0.001)(sin_df)

print(sin_df.__name__)
print(sin_df.__doc__)

df = sin_df(math.pi / 3)
print(df)
