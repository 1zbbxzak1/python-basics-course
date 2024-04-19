print('Задача 3. Отцы, матери и дети')

# Реализуйте два класса: «Родитель» и «Ребёнок».
#
# У родителя есть:
#     имя,
#     возраст,
#     список детей.
# И он может:
#     сообщить информацию о себе,
#     успокоить ребёнка,
#     покормить ребёнка.
#
# У ребёнка есть:
# имя,
# возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
# состояние спокойствия,
# состояние голода.
#
# Реализация состояний — на ваше усмотрение.
# Это может быть и простой «флаг», и словарь состояний, и что-то поинтереснее.

from enum import Enum


class Mood(Enum):
    calm = 1
    cry = 2

    def __str__(self):
        return self.name


class Satiety(Enum):
    full = 1
    hungry = 2

    def __str__(self):
        return self.name


class Child:

    def __init__(self, name: str, age: int, mood: Mood, satiety: Satiety):
        self.name = name
        self.age = age
        self.mood = mood
        self.satiety = satiety

    @property
    def is_calm(self) -> bool:
        return self.mood == Mood.calm

    @property
    def is_full(self) -> bool:
        return self.satiety == Satiety.full

    def __str__(self) -> str:
        return f'Меня зовут {self.name}, {self.age} лет. Настроение: {self.mood}, Сытость: {self.satiety}'


class Parent:

    def __init__(self, name: str, age: int, children: list[Child] = None):
        self.name = name
        self.age = age
        self.children = children or []

    def __str__(self) -> str:
        child_info = ", ".join(str(child) for child in self.children)
        return f'Меня зовут {self.name}, {self.age} лет. Дети: {child_info}'

    def calm_down(self, child: Child) -> None:
        child.mood = Mood.calm

    def feed(self, child: Child) -> None:
        child.satiety = Satiety.full

    def register_child(self, child: Child) -> None:
        if self.age < 16:
            raise ValueError('Родителю должно быть хотя бы 16 лет.')
        self.children.append(child)
