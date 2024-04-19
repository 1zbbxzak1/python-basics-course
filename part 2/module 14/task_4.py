print('Задача 4. Счётчик')

# Реализуйте декоратор counter, считающий и выводящий количество вызовов декорируемой функции.
#
# Для решения задачи нельзя использовать операторы global и nonlocal (об этом мы ещё расскажем).

import functools
import datetime


def logging_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print(f'Вызов функции: {func.__name__}')
            print(f'Документация функции: {func.__doc__}')
            return func(*args, **kwargs)
        except Exception as e:
            error_msg = f'Ошибка в функции {func.__name__}: {str(e)}\n'
            with open('function_errors.log', 'a', encoding="utf-8") as file:
                file.write(f'{datetime.datetime.now()}: {error_msg}')
            print(error_msg)

    return wrapper


def counter(func):
    count = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'Функция {func.__name__} была вызвана {count} раз')
        return func(*args, **kwargs)

    return wrapper


@logging_decorator
@counter
def example_function():
    """
    Это документация для функции example_function.
    """
    print('Выполнение функции...')


@logging_decorator
@counter
def another_function():
    """
    Это документация для функции another_function.
    """
    print(1 / 0)


example_function()
example_function()
another_function()
another_function()

print()
