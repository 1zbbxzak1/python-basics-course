print('Задача 5. Маятник ')

# Известно, что амплитуда качающегося маятника с каждым разом затухает
# на 8,4% от амплитуды прошлого колебания.
# Если качнуть маятник,
# то, строго говоря, он не остановится никогда,
# просто амплитуда будет постоянно уменьшаться до тех пор,
# пока мы не сочтём такой маятник остановившимся.

# Напишите программу,
# определяющую, сколько раз качнётся маятник, прежде чем он, по нашему мнению, остановится.

# Программа получает на вход
# начальную амплитуду колебания в сантиметрах
# и конечную амплитуду его колебаний,
# которая считается остановкой маятника.

# Обеспечьте контроль ввода.

# Пример:

# Введите начальную амплитуду: 1
# Введите амплитуду остановки: 0.1

# Маятник считается остановившимся через 27 колебаний

import math

start_amplitude = float(input('Введите начальную амплитуду: '))
stop_amplitude = float(input('Введите амплитуду остановки: '))

oscillations = math.ceil(-math.log(start_amplitude / stop_amplitude, 0.916))

print(f'Маятник считается остановившимся через {oscillations} колебаний')

print()