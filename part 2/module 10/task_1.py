print('Задача 1. Имена 2')

# Есть файл people.txt, в котором построчно хранится N имён пользователей.
#
# Напишите программу, которая берёт количество символов в каждой строке файла и в качестве ответа выводит общую сумму.
# Если в какой-либо строке меньше трёх символов (не считая литерала \n), то вызывается ошибка и сообщение,
# в какой именно строке она возникла. Программа при этом не завершается и обрабатывает все имена файла.
#
# Также при желании можно вывести все ошибки в отдельный файл errors.log.
#
# Пример работы программы
# Содержимое файла people.txt:
# Василий
# Николай
# Надежда
# Никита
# Ян
# Ольга
# Евгения
# Кристина
#
# Ответ в консоли:
# Ошибка: менее трёх символов в строке 5.
# Общее количество символов: 49.

def process_file(file_path, errors_log_path=None):
    total_characters = 0
    error_messages = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                line_length = len(line.strip())
                if line_length < 3:
                    error_message = f"Ошибка: менее трёх символов в строке {line_number}."
                    error_messages.append(error_message)
                    if errors_log_path:
                        with open(errors_log_path, 'a',
                                  encoding='utf-8') as errors_log:
                            errors_log.write(error_message + '\n')
                total_characters += line_length

    except (FileNotFoundError, Exception) as e:
        print(f"Ошибка: {e}.")
        return 0, []

    return total_characters, error_messages

def main():
    file_path, errors_log_path = 'people.txt', 'errors.log'
    total_characters, error_messages = process_file(file_path, errors_log_path)

    if error_messages:
        print(f"Детали ошибок записаны в файл {errors_log_path}.",
              '\n'.join(error_messages))
    print(f"Общее количество символов: {total_characters}.")

main()

print()