print('Задача 5. Песни')

# Мы пишем приложение для удобного прослушивания музыки.
# У Вани есть список из девяти песен группы Depeche Mode.
# В информацию о каждом треке входит название и продолжительность
# с точностью до долей минут:
#
# violator_songs = [['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43],
# ['Personal Jesus', 4.56], ['Halo', 4.9], ['Waiting for the Night', 6.07],
# ['Enjoy the Silence', 4.20], ['Policy of Truth', 4.76], ['Blue Dress', 4.29],
# ['Clean', 5.83]]
#
# Из этого списка Ваня хочет выбрать N песен и добавить их в особый плейлист
# с другими треками. При этом ему важно, сколько времени в сумме эти N песен
# будут звучать.
#
# Напишите программу, которая запрашивает у пользователя количество песен из списка
# и их названия, а на экран выводит общее время их звучания.
#
# Пример:
# Сколько песен выбрать? 3
# Название 1-й песни: Halo
# Название 2-й песни: Enjoy the Silence
# Название 3-й песни: Clean
# Общее время звучания песен — 14,93 минуты

violator_songs = [['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43],
                  ['Personal Jesus', 4.56], ['Halo', 4.9],
                  ['Waiting for the Night', 6.07], ['Enjoy the Silence', 4.20],
                  ['Policy of Truth', 4.76], ['Blue Dress', 4.29],
                  ['Clean', 5.83]]

songs_count = int(input("Сколько песен выбрать? "))
result_time = 0

for num in range(songs_count):
    user_song = input(f'Название {num + 1}-й песни: ')
    find = False
    for violator_song in violator_songs:
        if violator_song[0] == user_song:
            result_time += violator_song[1]
            find = True
    if not find:
        print('Ошибка. Песня не найдена в списке.')

print(f'Общее время звучания песен — {result_time:.2f} минуты.')

print()
