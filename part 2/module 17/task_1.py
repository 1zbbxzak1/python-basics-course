print('Задача 1. Новые списки')

# Даны три списка:
#
# floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
# names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
# numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
#
# Напишите код, который создаёт три новых списка. Вот их содержимое:
# Каждое число из списка floats возводится в третью степень и округляется до трёх знаков после запятой.
# Из списка names берутся только имена минимум из пяти букв.
# Из списка numbers берётся произведение всех чисел.

from typing import List

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

floats_cubed_and_rounded = [round(num**3, 3) for num in floats]
names_min_length_five = list(filter(lambda name: len(name) >= 5, names))
product_of_numbers = int(eval("*".join(map(str, numbers))))

print("Floats cubed and rounded:", floats_cubed_and_rounded)
print("Names with minimum length five:", names_min_length_five)
print("Product of numbers:", product_of_numbers)

print()
