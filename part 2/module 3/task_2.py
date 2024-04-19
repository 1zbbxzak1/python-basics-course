print('Задание 2. Уникальное объединение списков')

# Вы работаете в команде разработки программного обеспечения
# для компании, которая занимается обработкой и анализом данных.
# Ваша команда получает данные из различных источников, вам нужно объединить
# их в один отсортированный список для дальнейшей обработки.
# Однако источники данных возвращают отсортированные списки с возможными дубликатами,
# и ваша задача — создать программу, которая объединит эти списки
# в один отсортированный список без дубликатов.
#
# Напишите программу, которая объединяет два отсортированных списка целых чисел
# в один отсортированный список без дубликатов.


def merge_sorted_lists(first_list, second_list):
    first_list.extend(second_list)
    for element in first_list:
        while first_list.count(element) > 1:
            first_list.remove(element)

    first_list.sort()
    return first_list


first_list = input('Элементы первого массива (Вводить через пробел): ').split()
first_list = [int(item) for item in first_list]

second_list = input(
    'Элементы второго массива (Вводить через пробел): ').split()
second_list = [int(item) for item in second_list]

merged = merge_sorted_lists(first_list, second_list)
print(f"Вывод: {merged}")

print()
