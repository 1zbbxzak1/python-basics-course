print('Задача 6. Абстрактный класс')

# Создайте:
#     класс Shape, который будет базовым классом для всех фигур и будет хранить пустой метод area, который наследники должны переопределить;
#     класс Circle;
#     класс Rectangle;
#     класс Triangle.
#     Классы Circle, Rectangle и Triangle наследуют от класса Shape и реализуют метод для вычисления площади фигуры.
#
# Дополнительно: изучите информацию о работе с абстрактными классами.
#
# На основе этой информации сделайте так, чтобы:
#     Нельзя было создавать объекты класса Shape.
#     Наследники класса Shape переопределяли его метод area, чтобы объекты этих классов можно было использовать.

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Пример использования:
# shape = Shape()  # Это вызовет ошибку, так как Shape - абстрактный класс
circle = Circle(9)
rectangle = Rectangle(2, 8)
triangle = Triangle(5, 10)

print("Площадь круга:", circle.area())
print("Площадь прямоугольника:", rectangle.area())
print("Площадь треугольника:", triangle.area())
