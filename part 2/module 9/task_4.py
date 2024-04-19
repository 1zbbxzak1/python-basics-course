print('Задача 4. Турнир')

# В файле first_tour.txt записано число K и данные об участниках турнира по настольной игре «Орлеан»:
# фамилии, имена и количество баллов, набранных в первом туре. Во второй тур проходят участники,
# которые набрали более K баллов в первом туре.
#
# Напишите программу, которая выводит в файл second_tour.txt данные всех участников,
# прошедших во второй тур, с нумерацией.
#
# В первой строке нужно вывести в файл second_tour.txt количество участников второго тура.
# Затем программа должна вывести фамилии, инициалы и количество баллов всех участников, прошедших во второй тур,
# с нумерацией. Имя нужно сократить до одной буквы. Список должен быть отсортирован по убыванию набранных баллов.
#
# Пример:
# Содержимое файла first_tour.txt:
# 80
# Ivanov Serg 80
# Sergeev Petr 92
# Petrov Vasiliy 98
# Vasiliev Maxim 78
#
# Содержимое файла second_tour.txt:
# 2
# 1) V. Petrov 98
# 2) P. Sergeev 92

# Чтение данных из файла first_tour.txt
with open('first_tour.txt', 'r') as file:
    k = int(file.readline())
    participants = [line.split() for line in file.readlines()]

# Фильтрация участников, прошедших во второй тур
second_tour_participants = [
    participant for participant in participants if int(participant[2]) > k
]

# Сортировка участников по убыванию баллов
second_tour_participants.sort(key=lambda x: int(x[2]), reverse=True)

# Запись результатов в файл second_tour.txt
with open('second_tour.txt', 'w') as file:
    file.write(str(len(second_tour_participants)) + '\n')
    for i, participant in enumerate(second_tour_participants, start=1):
        file.write(
            f"{i}) {participant[1][0]}. {participant[0]} {participant[2]}\n")

print("Результаты записаны в файл second_tour.txt")

print()
