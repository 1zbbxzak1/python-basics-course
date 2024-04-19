print('Задача 6. Ход конём')

# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
#
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

print('Введите местоположение коня: ')
hor_x = int(float(input('X: ')) * 10) % 10
hor_y = int(float(input('Y: ')) * 10) % 10

print('Введите местоположение точки на доске: ')
dot_x = int(float(input('X: ')) * 10) % 10
dot_y = int(float(input('Y: ')) * 10) % 10
print(f'Конь в клетке ({hor_x}, {hor_y}). Точка в клетке ({dot_x}, {dot_y}).')

x_dif = abs(hor_x - dot_x)
y_dif = abs(hor_y - dot_y)

if x_dif == 2 and y_dif == 1 or x_dif == 1 and y_dif == 2:
    print('Да, конь может ходить в эту точку.')
else:
    print('Нет, конь не может ходить в эту точку')

print()