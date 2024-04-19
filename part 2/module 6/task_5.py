print('Задание 5. Словарь синонимов')

# Одна библиотека поручила вам написать программу для оцифровки словарей синонимов.
# На вход в программу подаётся N пар слов. Каждое слово является синонимом для своего парного слова.
#
# Реализуйте код, который составляет словарь синонимов (все слова в словаре различны),
# затем запрашивает у пользователя слово и выводит на экран его синоним.
# Обеспечьте контроль ввода: если такого слова нет, выведите ошибку и запросите слово ещё раз.
# При этом проверка не должна зависеть от регистра символов.
#
# Пример
# Введите количество пар слов: 3
# Первая пара: Привет — Здравствуйте
# Вторая пара: Печально — Грустно
# Третья пара: Весело — Радостно
# Введите слово: интересно
# Такого слова в словаре нет.
# Введите слово: здравствуйте
# Синоним: Привет


def create_synonyms_dict(num_pairs):
    synonyms_dict = {}

    for i in range(num_pairs):
        pair = input(f"Пара {i + 1}: ").split(' — ')
        word1, word2 = pair[0].lower(), pair[1].lower()
        synonyms_dict[word1] = word2
        synonyms_dict[word2] = word1

    return synonyms_dict


def find_synonym(synonyms_dict, word):
    return synonyms_dict.get(word.lower(), "Такого слова в словаре нет.")


num_pairs = int(input("Введите количество пар слов: "))

synonyms_dict = create_synonyms_dict(num_pairs)

while True:
    user_word = input("Введите слово: ")

    synonym = find_synonym(synonyms_dict, user_word)
    print(f"Синоним: {synonym}")

    repeat = input("Хотите продолжить? (да/нет): ")
    if repeat.lower() != 'да':
        break

print()
