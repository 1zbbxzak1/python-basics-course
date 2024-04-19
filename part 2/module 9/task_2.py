print('Задача 2. Дзен Пайтона')

# В файле zen.txt хранится так называемый Дзен Пайтона — текст философии
# программирования на языке Python.
#
# Напишите программу, которая выводит на экран все строки этого файла в обратном порядке.
#
# Пример:
# zen.txt
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
#
# Результат работы программы:
# Namespaces are one honking great idea -- let's do more of those!
# If the implementation is easy to explain, it may be a good idea.

with open('zen.txt', 'r') as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line.strip())

print()