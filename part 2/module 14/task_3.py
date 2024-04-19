print('Задача 3. Логирование')

# Реализуйте декоратор logging, который будет отвечать за логирование функций.
# На экран выводится название функции и её документация.
# Если во время выполнения декорируемой функции возникла ошибка,
# то в файл function_errors.log записываются название функции и ошибки.

# Также постарайтесь сделать так, чтобы программа не завершалась
# после обнаружения первой же ошибки,
# а обрабатывала все декорируемые функции и сразу записывала все ошибки в файл.

# Дополнительно: запишите дату и время возникновения ошибки, используя модуль datetime.

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


@logging_decorator
def example_function():
    """
    Это документация для функции example_function.
    """
    print('Выполнение функции...')


@logging_decorator
def another_function():
    """
    Это документация для функции another_function.
    """
    print(1 / 0)  # Генерируем ошибку деления на ноль


example_function()
another_function()

print()
