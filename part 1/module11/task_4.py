print('Задача 4. Первая цифра')

# Дано положительное действительное число X.
# Выведите его первую цифру после десятичной точки.
# При решении этой задачи нельзя пользоваться условной инструкцией, циклом или строками

num = float(input('Введите положительное действительное число: '))

print(f'Первая цифра после десятичной точки: {int(num * 10) % 10}')