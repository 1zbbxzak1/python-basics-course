print('Задача 1. Квадраты чисел')

# Пользователь вводит число N. Напишите программу, которая генерирует последовательность
# из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так далее).
# Реализацию напишите тремя способами: класс-итератор, функция-генератор и генераторное выражение.

n = int(input("Введите число N: "))


# 1. Класс-итератор:
class SquaresIterator:

    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current**2
        self.current += 1
        return result


squares_iterator = SquaresIterator(n)
squares_list_iterator = list(squares_iterator)
print(f'Класс-итератор: {squares_list_iterator}\n')


# 2. Функция-генератор:
def generate_squares(n):
    current = 1
    while current <= n:
        yield current**2
        current += 1


squares_generator = generate_squares(n)
squares_list_generator = list(squares_generator)
print(f'Функция-генератор: {squares_list_generator}\n')

# 3. Генераторное выражение:
squares_expression = (x**2 for x in range(1, n + 1))
squares_list_expression = list(squares_expression)
print(f'Генераторное выражение: {squares_list_expression}\n')

print()
