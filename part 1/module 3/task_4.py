print('Задача 4. Площадь треугольника')

# Напишите программу,
# которая запрашивает у пользователя длины двух катетов
# в прямоугольном треугольнике и выводит его площадь.

# Формула:
# S = ab/2

first_leg = int(input('Введите длину первого катета: '))
second_leg = int(input('Введите длину второго катета: '))

print(f'Площадь треугольника равна {first_leg * second_leg / 2}')
print()