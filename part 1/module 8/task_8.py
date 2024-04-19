print('Задача 8. Кинотеатр')

# X мальчиков и Y девочек пошли в кинотеатр
# и купили билеты на подряд идущие места в одном ряду.

# Напишите программу только с помощью цикла for на python,
# которая выдаст, как нужно сесть мальчикам и девочкам,
# чтобы рядом с каждым мальчиком сидела хотя бы одна девочка,
# а рядом с каждой девочкой — хотя бы один мальчик.

# На вход подаются два числа - кол-во мальчиков X и кол-во девочек Y.
# В ответе выведите какую-нибудь строку,
# в которой будет ровно X символов “B” (обозначающих мальчиков)
# и Y символов “G” (обозначающих девочек), удовлетворяющую условию задачи.
# Пробелы между символами выводить не нужно.
# Если рассадить мальчиков и девочек согласно условию задачи невозможно,
# выведите строку “Нет решения”.

# Пример 1:

# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 5
# Ответ: BGBGBGBGBG
# Ответ: BGBGBGBGBG

# Пример 2:

# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 3
# Ответ: BGBGBBGB

# Пример 3:

# Введите кол-во мальчиков: 100
# Введите кол-во девочек: 1
# Ответ: Нет решения

male_count = int(input('Введите кол-во мальчиков: '))
fem_count = int(input('Введите кол-во девочек: '))
result = ''

if (male_count > 2 * fem_count) or (fem_count > 2 * male_count):
    print('Нет решения')

elif male_count >= fem_count:
    count = male_count - fem_count
    for bgb in range(count):
        result += 'BGB'
    for bg in range(fem_count - count):
        result += 'BG'
else:
    count = fem_count - male_count
    for gbg in range(count):
        result += 'GBG'
    for gb in range(male_count - count):
        result += 'GB'
print(f'Ответ: {result}')