print('Задача 2. Математический модуль')

# Вася использует в своей программе очень много различных математических вычислений,
# связанных с фигурами. Например, нахождение их площадей или периметров.
# Поэтому, чтобы не захламлять код огромным количеством функций,
# он решил выделить для них отдельный класс, подключить как модуль и
# использовать по аналогии с модулем math.

# Реализуйте класс MyMath, состоящий как минимум из следующих методов
# (можете бонусом добавить и другие методы):
#
# вычисление длины окружности,
# вычисление площади окружности,
# вычисление объёма куба,
# вычисление площади поверхности сферы.

import math


class MyMath:

    @staticmethod
    def circle_len(radius: float) -> float:
        """
        Вычисляет длину окружности.

        Args:
        - radius (float): Радиус окружности

        Returns:
        - float: Длина окружности
        """
        return 2 * math.pi * radius

    @staticmethod
    def circle_sq(radius: float) -> float:
        """
        Вычисляет площадь окружности.

        Args:
        - radius (float): Радиус окружности

        Returns:
        - float: Площадь окружности
        """
        return math.pi * (radius**2)

    @staticmethod
    def cube_volume(side_length: float) -> float:
        """
        Вычисляет объем куба.

        Args:
        - side_length (float): Длина стороны куба

        Returns:
        - float: Объем куба
        """
        return side_length**3

    @staticmethod
    def sphere_surface_area(radius: float) -> float:
        """
        Вычисляет площадь поверхности сферы.

        Args:
        - radius (float): Радиус сферы

        Returns:
        - float: Площадь поверхности сферы
        """
        return 4 * math.pi * (radius**2)


res_1 = MyMath.circle_len(5)
res_2 = MyMath.circle_sq(6)
print(res_1)
print(res_2)

print()
