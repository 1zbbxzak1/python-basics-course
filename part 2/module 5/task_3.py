print('Задание 3. Файлы')

# В IT-компании есть негласные правила именования текстовых документов:
# Название файла не может начинаться с одного из специальных символов: @, №, $, %, ^, &, *, ().
# Файл должен заканчиваться расширением .txt или .docx.
# Напишите программу, которая получает на вход полное название файла и проверяет,
# соответствует ли он этим правилам.
#
# Пример 1
# Название файла: @example.txt.
# Ошибка: название начинается недопустимым символом.
#
# Пример 2
# Название файла: example.ttx.
# Ошибка: неверное расширение файла. Ожидалось .txt или .docx.
#
# Пример 3
# Название файла: example.txt.
# Файл назван верно.


def check_filename(file_name):
    disallowed_start_symbols = ['@', '№', '$', '%', '^', '&', '*', '(']
    if any(
            file_name.startswith(symbol)
            for symbol in disallowed_start_symbols):
        return "Ошибка: название начинается недопустимым символом."

    allowed_extensions = ['.txt', '.docx']
    if not any(file_name.endswith(ext) for ext in allowed_extensions):
        return "Ошибка: неверное расширение файла. Ожидалось .txt или .docx."

    return "Файл назван верно."


file_name = input("Название файла: ")
print(check_filename(file_name))

print()
