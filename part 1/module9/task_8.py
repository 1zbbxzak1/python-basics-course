print('Задача 8. Древний палиндром')

# Контекст:
# Вы молодой археолог, который исследует древний свиток с таинственным посланием.
# Согласно легенде, если вы сможете прочитать палиндром из этого послания, то раскроете его секреты.
# Однако свиток весьма постарел, и некоторые буквы стерлись.
# Вам нужно разработать программу, которая поможет определить, является ли фрагмент послания, введенный пользователем, палиндромом.
# Если ваша программа сможет справиться с заданием, то вы сможете приблизиться к разгадке древней тайны.
#
# Задача:
# Напишите программу, которая поможет определить, является ли введенная строка палиндромом.
# Если введенная строка является палиндромом, выведите сообщение "Да, это палиндром!".
# В противном случае выведите сообщение "Нет, это не палиндром!".
#
# Советы:
# -- Для выполнения задачи используйте цикл for и итерацию по символам строки.
# -- Возможно вам понадобиться развернуть строку, чтобы это сделать вам достаточно уметь проходить по строке циклом и использовать конкатенацию.
# -- Чтобы сложить символы строки в обратном порядке - подумайте над переменой мест слагаемых. Будут ли результаты одинаковы если мы все символы будем добавлять в конец строки (строка = строка + символ) и если мы будем их добавлять в начало строки (строка = символ + строка)?

string = input('Введите строку: ')
reversed_string = ''

for char in string:
    reversed_string = char + reversed_string

if string == reversed_string:
    print('Да, это палиндром!')
else:
    print('Нет, это не палиндром!')