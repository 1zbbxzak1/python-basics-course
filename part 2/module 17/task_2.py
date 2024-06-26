print('Задача 2. И снова zip')

# Помните, как нам приходилось что-то выдумывать, чтобы создать аналог функции zip?
# Теперь вы знаете, как это сделать в одну строку.
#
# Даны список букв (letters) и список цифр (numbers).
# Каждый список состоит из N элементов.
# Создайте кортежи из пар элементов списков и запишите их в список results.
# Не используйте функцию zip. Решите задачу в одну строку (не считая print(results)).

# Примеры списков:
# letters: List[str] = ['a', 'b', 'c', 'd', 'e']
# numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
#
# Результат работы программы:
# [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

letters = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

results = [(letters[i], numbers[i])
           for i in range(min(len(letters), len(numbers)))]

print(results)

print()
