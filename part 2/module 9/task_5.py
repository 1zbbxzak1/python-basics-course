print('Задача 5. Частотный анализ')

# Есть файл text.txt, который содержит текст. Напишите программу, которая
# выполняет частотный анализ, определяя долю каждой буквы английского алфавита в общем
# количестве английских букв в тексте, и выводит результат в файл analysis.txt.
# Символы, не являющиеся буквами английского алфавита, учитывать не нужно.
#
# В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с тремя
# знаками в дробной части. Буквы должны быть отсортированы по убыванию их доли.
# Буквы с равной долей должны следовать в алфавитном порядке.
#
# Пример:
# Содержимое файла text.txt:
# Mama myla ramu.
#
# Содержимое файла analysis.txt:
# a 0.333
# m 0.333
# l 0.083
# r 0.083
# u 0.083
# y 0.083

from collections import Counter


def calculate_letter_frequencies(text):
    cleaned_text = ''.join(char.lower() for char in text
                           if char.isalpha() and char.isascii())
    total_letters = len(cleaned_text)

    frequencies = [(letter, count / total_letters)
                   for letter, count in sorted(Counter(cleaned_text).items(),
                                               key=lambda x: (-x[1], x[0]))]
    return frequencies


def write_analysis_results(frequencies, output_file='analysis.txt'):
    with open(output_file, 'w') as file:
        file.writelines(f"{letter} {frequency:.3f}\n"
                        for letter, frequency in frequencies)


with open('text.txt', 'r') as file:
    text_content = file.read()

frequencies = calculate_letter_frequencies(text_content)
write_analysis_results(frequencies)
print("Результаты анализа записаны в файл analysis.txt")

print()