print('Задача 4. Магия')

# Для одной игры необходимо реализовать механику магии, где при соединении двух элементов получается новый.
# У нас есть четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля».
# Из них получаются новые: «Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава».
#
# Таблица преобразований:
#     Вода + Воздух = Шторм;
#     Вода + Огонь = Пар;
#     Вода + Земля = Грязь;
#     Воздух + Огонь = Молния;
#     Воздух + Земля = Пыль;
#     Огонь + Земля = Лава.
#
# Напишите программу, которая реализует все эти элементы.
# Каждый элемент необходимо организовать как отдельный класс. Если результат не определён, то возвращается None.


class Element:

    def __init__(self, name):
        self.name = name

    def combine(self, other):
        combinations = {
            ('Вода', 'Воздух'): Storm(),
            ('Вода', 'Огонь'): Steam(),
            ('Вода', 'Земля'): Mud(),
            ('Воздух', 'Огонь'): Lightning(),
            ('Воздух', 'Земля'): Dust(),
            ('Огонь', 'Земля'): Lava(),
        }
        return combinations.get((self.name, other.name), None)

    def __add__(self, other):
        if isinstance(other, Element):
            return self.combine(other)
        else:
            return None

    def __str__(self):
        return self.name


class Water(Element):

    def __init__(self):
        super().__init__('Вода')


class Air(Element):

    def __init__(self):
        super().__init__('Воздух')


class Fire(Element):

    def __init__(self):
        super().__init__('Огонь')


class Earth(Element):

    def __init__(self):
        super().__init__('Земля')


class Storm(Element):

    def __init__(self):
        super().__init__('Шторм')


class Steam(Element):

    def __init__(self):
        super().__init__('Пар')


class Mud(Element):

    def __init__(self):
        super().__init__('Грязь')


class Lightning(Element):

    def __init__(self):
        super().__init__('Молния')


class Dust(Element):

    def __init__(self):
        super().__init__('Пыль')


class Lava(Element):

    def __init__(self):
        super().__init__('Лава')


# Пример использования
water = Water()
air = Air()
fire = Fire()
earth = Earth()

# Комбинации
result1 = water + air
result2 = water + fire
result3 = water + earth
result4 = air + fire
result5 = air + earth
result6 = fire + earth

# Вывод результата
print(f"{water} + {air} = {result1}")
print(f"{water} + {fire} = {result2}")
print(f"{water} + {earth} = {result3}")
print(f"{air} + {fire} = {result4}")
print(f"{air} + {earth} = {result5}")
print(f"{fire} + {earth} = {result6}")

print()
