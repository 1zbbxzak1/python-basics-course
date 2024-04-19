print('Задание 8. Снова палиндром')

# Пользователь вводит строку. Необходимо написать программу, которая определяет,
# существует ли у этой строки перестановка, при которой она станет палиндромом.
# Затем она должна выводить соответствующее сообщение.
#
# Пример 1
# Введите строку: aab
# Можно сделать палиндромом
#
# Пример 2
# Введите строку: aabc
# Нельзя сделать палиндромом


def can_be_palindrome(s):
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    odd_count = sum(count % 2 != 0 for count in char_count.values())

    return odd_count <= 1


user_input = input("Введите строку: ")

if can_be_palindrome(user_input):
    print("Можно сделать палиндромом")
else:
    print("Нельзя сделать палиндромом")
