print('Задача 6. Проверяем бухгалтера')

# Реализуйте программу,
# которая запрашивает два числа у пользователя.
# После этого у каждого числа возьмите две последние цифры.
# Получившиеся два числа сложите и выведите на экран.

# Пример:
# Введите первое число: 456
# Введите второе число: 123
# Сумма: 79

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

first_number = str(first_number)
second_number = str(second_number)

first_number = first_number[-2:]
second_number = second_number[-2:]

print('Сумма:', int(first_number) + int(second_number))