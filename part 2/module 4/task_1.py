print('Задание 1. Гласные буквы')

# Команде лингвистов понравилось качество ваших программ, поэтому они решили
# заказать функцию для анализатора текста, которая создавала бы список гласных букв
# в нём и считала бы их количество.
#
# Напишите программу, которая запрашивает у пользователя текст
# и генерирует список гласных букв этого материала (сама строка вводится на русском языке).
# Выведите в консоль сам список и его длину.
#
# Пример:
# Введите текст: Нужно отнести кольцо в Мордор!
# Список гласных букв: ['у', 'о', 'о', 'е', 'и', 'о', 'о', 'о', 'о']
# Длина списка: 9


# Функция для создания списка гласных букв и подсчета их количества
def analyze_vowels(text):
    vowels = "аеёиоуыэюя"  # Гласные буквы в русском алфавите
    vowels_list = [char for char in text.lower() if char in vowels]
    return vowels_list


# Получение текста от пользователя
user_text = input("Введите текст на русском языке: ")

# Анализ гласных букв и вывод результатов
vowels_result = analyze_vowels(user_text)
print("Список гласных букв:", vowels_result)
print("Длина списка:", len(vowels_result))

print()
