print('Задача 1. Сумма чисел 2')

# Во входном файле numbers.txt записано N целых чисел, которые могут быть
# разделены пробелами и концами строк. Напишите программу, которая выводит
# сумму чисел во выходной файл answer.txt.
#
# Пример:
# Содержимое файла numbers.txt
#     2
#2
#  2
#        2
# Содержимое файла answer.txt
# 8

# Чтение из входного файла numbers.txt
with open('numbers.txt', 'r') as input_file:
    lines = input_file.readlines()

# Обработка и суммирование чисел
total_sum = sum(int(line) for line in lines if line.strip().isdigit())

# Запись результата в выходной файл answer.txt
with open('answer.txt', 'w') as output_file:
    output_file.write(str(total_sum))

print('Результат записан в answer.txt')

print()