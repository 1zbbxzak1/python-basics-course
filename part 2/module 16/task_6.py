print('Задача 6. Класс-декоратор')

# Создайте декоратор, который логирует аргументы, результаты и время выполнения функции.
#
# Реализуйте декоратор как класс и примените его к функции complex_algorithm.
# Запустите задекорированную функцию и проверьте время её выполнения.

import time


class LoggerDecorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()

        print(f"Вызов функции {self.func.__name__}")
        print(f"Аргументы: {args}, {kwargs}")

        result = self.func(*args, **kwargs)

        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Результат: {result}")
        print(f"Время выполнения: {execution_time} секунд")

        return result


@LoggerDecorator
def complex_algorithm(arg1, arg2):
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result


# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)
