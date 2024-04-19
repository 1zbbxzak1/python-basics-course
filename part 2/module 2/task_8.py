print('Задание 8. Сортировка')

# Дан список из N чисел. Напишите программу, которая сортирует
# элементы списка по возрастанию и выводит их на экран.
# Дополнительный список использовать нельзя.
#
# Постарайтесь придумать и написать как можно более эффективный алгоритм сортировки.
#
# Пример:
# Изначальный список: [1, 4, –3, 0, 10]
# Отсортированный список: [–3, 0, 1, 4, 10]

def bubble_sort(input_list):
    length = len(input_list)
    if length <= 1:
        return input_list

    for i in range(length - 1):
        for j in range(i + 1, length):
            if input_list[j] < input_list[i]:
                input_list[i], input_list[j] = input_list[j], input_list[i]

    return input_list

user_input = input('Введите элементы списка через пробел: ').split()
integer_list = [int(item) for item in user_input]

sorted_list = bubble_sort(integer_list)
print(f'Отсортированный список: {sorted_list}')

print()