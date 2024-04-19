print('Задание 7. Считалка')

# N человек, пронумерованных числами от 1 до N, стоят в кругу.
# Они начинают играть в считалку на выбывание.
# Каждый K-й по счёту человек выходит из круга, после чего счёт продолжается
# со следующего за ним человека.
#
# На вход подаётся количество человек N и номер K.
# Напишите программу, которая выводит число от 1 до N — это номер человека,
# который останется в кругу последним.
#
# Пример:
# Количество человек: 5
# Какое число в считалке? 7
# Значит, выбывает каждый 7-й человек
#
# Текущий круг людей: [1, 2, 3, 4, 5]
# Начало счёта с номера 1
# Выбывает человек под номером 2
# ...
# Остался человек под номером 4


def last_person_standing(n, k):
    people = list(range(1, n + 1))
    current_index = 0

    while len(people) > 1:
        print(f'\nТекущий круг людей: {people}')
        print(f'Начало счёта с номера {people[current_index % len(people)]}')

        current_index = (current_index + k - 1) % len(people)
        print(f'Выбывает человек под номером {people.pop(current_index)}')

    return people[0]


# Ввод данных от пользователя
num_people = int(input('Количество человек: '))
k_value = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {k_value}-й человек')

result = last_person_standing(num_people, k_value)
print(f'\nОстался человек под номером {result}')

print()
