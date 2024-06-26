print('Задача 5. Текстовый редактор')

# Мы продолжаем разрабатывать новый текстовый редактор,
# и в этот раз нам поручили написать для него код,
# который считает количество любой буквы
# и любой цифры в тексте (а не только буквы Ы как раньше).
#
# Напишите функцию count_letters,
# которая принимает на вход текст и подсчитывает,
# какое в нём количество цифр K и букв N.
#
# Функция должна вывести на экран информацию
# о найденных буквах и цифрах в определенном формате.
#
# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищём? л
#
# Количество цифр 0: 2
# Количество букв л: 1

text = input('Введите текст: ')
dig = input('Какую цифру ищем? ')
let = input('Какую букву ищём? ')

def count_letters(text, let, dig):
    count_dig = 0
    count_let = 0
    for symbol in text:
        if symbol == let:
            count_let += 1
        elif symbol == dig:
            count_dig += 1
    print(f'Количество цифр {dig}: {count_dig}')
    print(f'Количество букв {let}: {count_let}')

count_letters(text, let, dig)

print()