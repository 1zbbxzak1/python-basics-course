print('Задача 5. Вася хочет выигрывать')

# Вася вдохновился фильмом «Двадцать одно» и решил изучить математику игровых автоматов. Для анализа данных ему нужна информация о том, как часто в автомате выпадает три или две одинаковых картинки. Для сбора данных нужна программа, проверяющая это равенство.

# Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести один из вариантов:
# 1) 3 (если все совпадают)
# 2) 2 (если два совпадают)
# 3) 0 (если все числа разные)

first = int(input('Введите первую картинку: '))
second = int(input('Введите вторую картинку: '))
third = int(input('Введите третью картинку: '))

if first == second and second == third:
    print('3 (все совпадают)')
elif first == second or second == third or first == third:
    print('2 (два совпадают)')
else:
    print('0 (все числа разные)')

print()