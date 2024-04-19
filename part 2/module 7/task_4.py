print('Задача 4. По парам')

# Напишите программу, которая инициализирует список из 10 случайных целых чисел,
# а затем делит эти числа на пары кортежей внутри списка. Выведите результат на экран.
#
# Дополнительно: решите задачу несколькими способами.
#
# Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]

import random

original_list = [random.randint(0, 9) for _ in range(10)]
new_list = [(original_list[i], original_list[i + 1])
            for i in range(0, len(original_list), 2)]

print("Оригинальный список:", original_list)
print("Новый список:", new_list)

original_list = [random.randint(0, 9) for _ in range(10)]
new_list = [
    tuple((original_list[i], original_list[i + 1]))
    for i in range(0, len(original_list), 2) if i + 1 < len(original_list)
]

print("Оригинальный список:", original_list)
print("Новый список:", new_list)

print()
