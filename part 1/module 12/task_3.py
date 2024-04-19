print('Задача 3. Апгрейд калькулятора')

# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только обычные арифметические действия.
# Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.

# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом: вывести сумму его цифр, максимальную или минимальную цифру.

#Каждое действие оформите в виде отдельной функции, а основную программу зациклите.

# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.

num = input('Введите число: ')


def sum_of_digits(num):
    sum = 0
    for dig in num:
        sum += int(dig)
    print(f'Сумма цифр числа {num} равна {sum}')


def max_of_digits(num):
    max_dig = 0
    for dig in num:
        max_dig = max(max_dig, int(dig))
    print(f'Максимальная цифра в числе {num} равна {max_dig}')


def min_of_digits(num):
    min_dig = 9
    for dig in num:
        min_dig = min(min_dig, int(dig))
    print(f'Минимальная цифра в числе {num} равна {min_dig}')


while True:
    action = input('Введите действие (sum, max, min) или завершите (end): ')
    if action == 'sum':
        sum_of_digits(num)
    elif action == 'max':
        max_of_digits(num)
    elif action == 'min':
        min_of_digits(num)
    elif action == 'end':
        break
    else:
        print('Неверное действие. Попробуйте ещё раз.')

print()
