print('Задача 1. Сумма чисел')

# Напишите функцию summa_n,
# которая принимает одно целое положительное число N
# и выводит сумму всех чисел от 1 до N включительно.
#
# Пример работы программы:
# Введите число: 5
#
# Я знаю, что сумма чисел от 1 до 5 равна 15

N = int(input('Введите число: '))

def summa_n(N):
    sum = 0
    for number in range(1, N + 1):
        sum += number
    print(f'Я знаю, что сумма чисел от 1 до {N} равна {sum}')

summa_n(N)

print()