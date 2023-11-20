print('Задача 4. Отрезок')

# Напишите программу, которая считывает с клавиатуры три числа a, b и c, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу c.

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_number = int(input('Введите третье число: '))

total = 0
count = 0

for num in range(first_number, second_number + 1):
    if num % third_number == 0:
        total += num
        count += 1

if count == 0:
    print(f'Нет чисел, кратных {third_number}')
else:
    print(f'Среднее арифметическое всех чисел из отрезка [{first_number}, {second_number}] равно {total / count}')