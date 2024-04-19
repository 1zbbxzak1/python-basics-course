print('Задача 4. Уникальный шифр')

# Напишите функцию, которая принимает строку и
# возвращает количество уникальных символов в строке.
# Используйте для выполнения задачи lambda-функции и map и/или filter.
#
# Сделайте так, чтобы алгоритм НЕ был регистрозависим:
# буквы разного регистра должны считаться одинаковыми.

from collections import Counter


def count_unique_characters(element: str) -> int:
    return sum(
        list(
            filter(lambda value: value == 1,
                   Counter(element.lower()).values())))


# Пример использования:
message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)
print(f"Количество уникальных символов в строке - {unique_count}")
