print('Задача 3. Число наоборот 2')

# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример:

# Введите первое число: 102
# Введите второе число: 123

# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225

def reversed_num(num):
    reversed_number = 0
    while num > 0:
        reversed_number = reversed_number * 10 + num % 10
        num = num // 10
    return reversed_number

first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))

print('Первое число наоборот:', reversed_num(first_num))
print('Второе число наоборот:', reversed_num(second_num))
print('Сумма:', reversed_num(first_num) + reversed_num(second_num))
print('Сумма наоборот:',
      reversed_num(reversed_num(first_num) + reversed_num(second_num)))

print()