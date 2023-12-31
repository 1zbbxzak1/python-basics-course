print('Задача 7. Пропавшая карточка')

# Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
#
# Вводится число N,
# далее еще N − 1 чисел:
# номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.

# Пример:
# Введите количество карточек: 5
# Введите номер оставшейся карточки: 1
# Введите номер оставшейся карточки: 4
# Введите номер оставшейся карточки: 5
# Введите номер оставшейся карточки: 3

# Номер пропавшей карточки: 2

n = int(input('Введите количество карточек: '))
sum_cards = 0

for card in range(n - 1):
    sum_cards += int(input('Введите номер оставшейся карточки: '))

lost_card = ((n * (n + 1)) // 2) - sum_cards

print(f'Номер пропавшей карточки: {lost_card}')