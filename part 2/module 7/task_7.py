print('Задача 7. Своя функция zip')

# В самом конце собеседования вам неожиданно сказали: «Расскажите, что делает функция zip».
# Чтобы произвести впечатление, вы решили не только рассказать о ней, но и написать её аналог.
#
# Даны строка и кортеж из чисел. Напишите программу, которая создаёт генератор из пар кортежей «символ — число».
# Затем выведите на экран сам генератор и кортежи.
#
# Пример:
# Строка: abcd
# Кортеж чисел: (10, 20, 30, 40)
#
# Результат:
# <generator object <genexpr> at 0x00000204A4234048>
# ('a', 10)
# ('b', 20)
# ('c', 30)
# ('d', 40)


def create_generator(s, nums):
    return ((char, num) for char, num in zip(s, nums))


# Пример использования
string_input = 'abcd'
tuple_numbers = (10, 20, 30, 40)

result_generator = create_generator(string_input, tuple_numbers)

print(result_generator)
for pair in result_generator:
    print(pair)
