print('Задача 2. Замедление кода')

# Реализуйте декоратор, который перед выполнением декорируемой функции
# ждёт несколько секунд.

import functools
import time


def delay_before_execution(seconds):

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Ждем {seconds} секунд перед выполнением функции...")
            time.sleep(seconds)
            return func(*args, **kwargs)

        return wrapper

    return decorator


# Используем декоратор с различными значениями задержки
@delay_before_execution(2)
def test1():
    print("Функция 1 выполняется.")


@delay_before_execution(5)
def test2():
    print("Функция 2 выполняется.")


# Проверка работы декоратора
test1()
test2()

print()
