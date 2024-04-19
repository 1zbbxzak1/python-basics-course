print('Задача 6. «Война и мир»')

# Мало кто не знает знаменитый роман Л. Н. Толстого «Война и мир».
# Это довольно объёмное произведение лежит в архиве voina-i-mir.zip.
# Напишите программу, которая подсчитывает статистику по буквам
# (не только русского алфавита) в этом романе и выводит результат на экран (или в файл).
# Результат должен быть отсортирован по частоте встречаемости букв
# (по возрастанию или убыванию). Регистр символов имеет значение.

from collections import Counter

with open('voina-i-mir.txt', 'r', encoding='utf-8') as file:
    content = file.read()

letter_statistics = Counter(char for char in content if char.isalpha())

sorted_statistics = sorted(letter_statistics.items(),
                           key=lambda x: (-x[1], x[0]))

with open('letter_statistics.txt', 'w', encoding='utf-8') as output_file:
    for letter, count in sorted_statistics:
        output_file.write(f"{letter}: {count}\n")

print("Статистика по буквам записана в файл letter_statistics.txt.")
