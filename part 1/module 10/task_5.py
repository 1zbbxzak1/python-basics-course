print('Задача 5. Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

N = int(input('Введите количество чисел: '))
max_num = 0
max_total_sum = 0

for number in range(N):
    total_sum = 0
    num = int(input('Введите число: '))

    if num > max_num:
        max_num = num

    while num > 0:
        total_sum += num % 10
        num //= 10

    if total_sum > max_total_sum:
        max_total_sum = total_sum

print(f'Наибольшее число: {max_num}')
print(f'Сумма цифр: {max_total_sum}')

print()
