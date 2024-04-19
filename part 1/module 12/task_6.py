print('Задача 6. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел

def gcd(first_num, second_num):
    while first_num != 0 and second_num != 0:
        if first_num > second_num:
            first_num = first_num % second_num
        else:
            second_num = second_num % first_num
        print(f'Наибольший общий делитель: {first_num + second_num}')

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

gcd(first_number, second_number)

print()
