print('Задача 2. Счастливое число')

# Напишите программу, которая запрашивает у пользователя число до тех пор, пока сумма запрашиваемых чисел
# не станет больше либо равна 777. Каждое введённое число при этом дозаписывается в файл out_file.txt.
# Сделайте так, чтобы перед дозаписью программа с вероятностью 1 к 13 выдавала пользователю случайное исключение и завершалась.
#
# Пример 1
# Введите число: 10
# Введите число: 500
# Введите число: 200
# Введите число: 67
# Вы успешно выполнили условие для выхода из порочного цикла!
# Содержимое файла out_file.txt:
# 10
# 500
# 200
# 67
#
# Пример 2
# Введите число: 10
# Введите число: 500
# Вас постигла неудача!
# Содержимое файла out_file.txt:
# 10

import random

out_file_path = 'out_file.txt'
total_sum = 0

try:
    with open(out_file_path, 'a') as out_file:
        while total_sum < 777:
            try:
                user_input = int(input("Введите число: "))
                out_file.write(f"{user_input}\n")
                total_sum += user_input

                if random.randint(1, 13) == 13: raise Exception

            except ValueError:
                print("Ошибка: Введите корректное число.")

    print("Вы успешно выполнили условие для выхода из порочного цикла!")

except Exception:
    print("Вас постигла неудача!")

finally:
    with open('out_file.txt', 'r', encoding='UTF-8') as out_file:
        print('Содержимое файла out_file.txt:')
        print(out_file.read())

print()
