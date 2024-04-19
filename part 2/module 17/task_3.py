print('Задача 3. Палиндром: возвращение')

# Есть множество встроенных и внешних библиотек для работы с данными в Python.
# С некоторыми из них вы уже работали. Например, с модулем collections,
# когда использовали специальный класс OrderedDict,
# с помощью которого делали упорядоченный словарь.
# В этой библиотеке есть и другие возможности, но их немного.
#
# Используя модуль collections, реализуйте функцию can_be_poly,
# которая принимает на вход строку и проверяет, можно ли получить из неё палиндром.

from collections import Counter


def can_be_poly(s):
    char_count = Counter(s)
    odd_count = sum(count % 2 != 0 for count in char_count.values())

    return odd_count <= 1


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))

print()
