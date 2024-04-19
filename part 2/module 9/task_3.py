print('Задача 3. Файлы и папки')

# Напишите программу, которая получает на вход путь до каталога
# (в том числе это может быть просто корень диска) и выводит общее количество файлов
# и подкаталогов в нём. Также выведите на экран размер каталога в килобайтах
# (1 килобайт = 1024 байт).
#
# Важный момент: чтобы посчитать, сколько весит каталог, нужно найти сумму размеров всех
# вложенных в него файлов.
#
# Результат работы программы на примере python_basic\Module14:
# E:\PycharmProjects\python_basic\Module14
# Размер каталога (в Кбайтах): 8.373046875
# Количество подкаталогов: 7
# Количество файлов: 15

import os


def get_file_stat(path):
    if os.path.isdir(path):
        total_weight, total_subdirs, total_files = 0, 1, 0

        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            weight, subdirs, files = get_file_stat(file_path)
            total_weight += weight
            total_files += files

        return total_weight, total_subdirs + len(os.listdir(path)), total_files

    return os.path.getsize(path), 0, 1


user_path = input('Укажите абсолютный путь: ')
weight, subdirs, files = get_file_stat(user_path)

print(f'Размер каталога (в Кбайтах): {weight / 1024}')
print(f'Количество подкаталогов: {subdirs}')
print(f'Количество файлов: {files}')

print()