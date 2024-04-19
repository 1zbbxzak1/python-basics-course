print('Задание 1. Песни — 2')

# Продолжим писать приложение для удобного прослушивания музыки, но теперь песни
# хранятся в виде словаря, а не в виде вложенных списков.
# Каждая песня состоит из названия и продолжительности с точностью до долей минут.
#
# Напишите программу, которая запрашивает у пользователя количество песен из списка
# и их названия, а на экран выводит общее время их звучания.
#
# Пример
# Сколько песен выбрать? 3
# Название первой песни: Halo
# Название второй песни: Enjoy the Silence
# Название третьей песни: Clean
# Общее время звучания песен: 14,93 минуты

violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}


def calculate_total_time(song_list):
    total_time = 0
    for song_name in song_list:
        if song_name in violator_songs:
            total_time += violator_songs[song_name]
        else:
            print(f'Песня "{song_name}" не найдена.')

    return total_time


count_songs = int(input('Сколько песен выбрать? '))
song_list = [input('Название песни: ') for _ in range(count_songs)]

total_time = calculate_total_time(song_list)
print(f'Общее время звучания песен: {total_time:.2f}')

print()
