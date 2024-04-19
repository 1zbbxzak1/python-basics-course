print('Задание 6. Ролики')

# Частная контора даёт в прокат ролики самых разных размеров.
# Человек может надеть ролики только своего размера.
#
# Пользователь вводит два списка размеров:
# N размеров роликов и K размеров ног людей.
# Реализуйте код, который определяет, какое наибольшее число человек может
# одновременно взять ролики и пойти кататься.
#
# Пример:
# Количество роликов: 4
# Размер пары 1: 41
# Размер пары 2: 40
# Размер пары 3: 39
# Размер пары 4: 42
# Количество людей: 3
# Размер ноги человека 1: 42
# Размер ноги человека 2: 41
# Размер ноги человека 3: 42
# Наибольшее количество людей, которые могут взять ролики: 2


def max_people_with_skates(skates, feet_sizes):
    skates.sort()
    feet_sizes.sort()

    max_people = 0
    skates_index = 0

    for size in feet_sizes:
        while skates_index < len(skates) and skates[skates_index] < size:
            skates_index += 1
        if skates_index < len(skates):
            max_people += 1
            skates_index += 1

    return max_people


# Ввод размеров роликов
num_skates = int(input('Количество роликов: '))
skates = [int(input(f'Размер пары {i + 1}: ')) for i in range(num_skates)]

# Ввод размеров ног людей
num_people = int(input('Количество людей: '))
feet_sizes = [
    int(input(f'Размер ноги человека {i + 1}: ')) for i in range(num_people)
]

result = max_people_with_skates(skates, feet_sizes)
print(f'Наибольшее количество людей, которые могут взять ролики: {result}')

print()
