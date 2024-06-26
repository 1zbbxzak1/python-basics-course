print('Задача 2. Пути файлов')

# Реализуйте функцию gen_files_path, которая рекурсивно проходит по всем каталогам указанной директории
# (по умолчанию — корневой диск), находит указанный пользователем каталог и генерирует пути всех встреченных файлов.
# В решении не нужно использовать рекурсию.

import os


def gen_files_path(directory='C:/'):
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)


# Пример использования
for file_path in gen_files_path('C:/Users'):
    print(file_path)

print()
