print('Задание 9. Анализ комментариев')

# Вы разрабатываете программу, которая анализирует тексты, написанные пользователем,
# и выдаёт статистику по использованию заглавных и строчных букв.
#
# Это может быть полезно, например, при анализе комментариев в социальных сетях
# или обработке текстовых данных для исследований.
#
# Задача
# Напишите программу, которая считывает строку и выводит количество заглавных и строчных букв
# в строке, используя методы строк.
#
# Программа должна это делать за один проход по строке.
#
# Решение должно быть оформлено в виде функции, которая принимает на вход строку-текст,
# а на выход возвращает два числа (количество заглавных и строчных букв).


def count_case_letters(text):
    uppercase_count = 0
    lowercase_count = 0

    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count


user_input = input("Введите строку: ")

uppercase, lowercase = count_case_letters(user_input)
print(f"Количество заглавных букв: {uppercase}")
print(f"Количество строчных букв: {lowercase}")
