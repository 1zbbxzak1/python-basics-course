print('Задание 4. Гистограмма частоты — 2')

# Вы уже писали программу для лингвистов, которая получала на вход текст и считала,
# сколько раз каждый символ встречается в строке.
# Теперь задание изменилось: максимальную частоту выводить не нужно, но необходимо написать
# функцию, которая будет инвертировать полученный словарь.
# То есть в качестве ключа будет частота, а в качестве значения — список символов с этой частотой.
#
# По итогу нужно реализовать следующие подзадачи:
#
# получить текст и создать из него оригинальный словарь частот;
# создать новый словарь и заполнить его данными из оригинального словаря частот,
# используя количество повторов в качестве ключей, а буквы — в качестве значений,
# добавляя их в список для хранения.
#
# Пример
# Введите текст: Здесь что-то написано
# Инвертированный словарь частот:
# 1 : ['З', 'д', 'е', 'ь', 'ч', '-', 'п', 'и']
# 2 : ['с', ' ', 'т', 'н', 'а']
# 3 : ['о']


def invert_frequency_dict(text):
    char_count = {}

    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    inverted_dict = {}
    for char, count in char_count.items():
        inverted_dict.setdefault(count, []).append(char)

    return inverted_dict


user_text = input("Введите текст: ")

inverted_frequency_dict = invert_frequency_dict(user_text)

print("Инвертированный словарь частот:")
for count, chars_list in inverted_frequency_dict.items():
    print(f"{count} : {chars_list}")

print()
