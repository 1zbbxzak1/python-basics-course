print('Задача 8. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_number = int(input('Введите третье число: '))

if first_number > second_number and first_number > third_number:
    print('Максимальное число:', first_number)
elif second_number > first_number and second_number > third_number:
    print('Максимальное число:', second_number)
else:
    print('Максимальное число:', third_number)