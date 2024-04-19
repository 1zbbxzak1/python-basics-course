print('Задача 4. Весь мир — декоратор…')

# Реализуйте декоратор для декораторов: он должен декорировать другую функцию,
# которая должна быть декоратором, и даёт возможность любому декоратору принимать
# произвольные аргументы.

from functools import wraps
from typing import Callable


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:

    @wraps(decorator)
    def wrapper(*args, **kwargs) -> Callable:
        return lambda func: decorator(func, *args, **kwargs)

    return wrapper


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):

    @wraps(func)
    def wrapper(*args_wrap, **kwargs_wrap):
        print(f"Переданные арги и кварги в декоратор: {args}, {kwargs}")
        return func(*args_wrap, **kwargs_wrap)

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int):
    print("Привет", text, num)


decorated_function("Юзер", 101)

print()
