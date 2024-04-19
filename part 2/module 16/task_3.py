print('Задача 3. Логирование в формате')

# Реализуйте декоратор, который будет логировать все методы декорируемого класса 
# (кроме магических методов) и в который можно передавать 
# формат вывода даты и времени логирования.

from datetime import datetime
import time


def log_method_execution(cls, func, fmt_str):
    """Декоратор для логирования вызываемого метода класса."""

    def log_and_execute(*args, **kwargs):
        try:
            method_name = f'{cls.__name__}.{func.__name__}'
            print(f'Запускается "{method_name}". '
                  f'Дата и время запуска: {datetime.now().strftime(fmt_str)}')
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time() - start
            print(f'Завершение "{method_name}", время работы = {round(end, 3)}s')
            return result
        except Exception as e:
            print(f'Произошла ошибка в методе {cls.__name__}.{func.__name__}: {e}')
            raise
    
    return log_and_execute
    

def log_methods(fmt_str: str):
    """Декоратор для логирования класса."""

    def decorator(cls):
        for method in dir(cls):
            if method.startswith('__'):
                continue
            value = getattr(cls, method)
            if callable(value):
                decorated = log_method_execution(cls, value, fmt_str)
                setattr(cls, method, decorated)
        return cls

    return decorator


@log_methods("%b %d %Y — %H:%M:%S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num * 2 for i_num in range(10000)])
        return result


@log_methods("%b %d %Y — %H:%M:%S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num * 2 for i_num in range(10000)])
        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()

print()