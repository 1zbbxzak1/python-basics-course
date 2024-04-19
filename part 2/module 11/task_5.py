print('Задача 5. Совместное проживание')

# Чтобы понять, стоит ли ему жить с кем-то или лучше остаться в гордом одиночестве,
# Артём решил провести необычное исследование. Для этого он реализовал модель человека и модель дома.
#
# Человек может (должны быть такие методы):
#     есть (+ сытость, − еда);
#     работать (− сытость, + деньги);
#     играть (− сытость);
#     ходить в магазин за едой (+ еда, − деньги);
#     прожить один день (выбирает одно действие согласно описанному ниже приоритету и выполняет его).
#
# У человека есть (должны быть такие атрибуты):
#     имя,
#     степень сытости (изначально 50),
#     дом.
#
#
# В доме есть:
#     холодильник с едой (изначально 50 еды),
#     тумбочка с деньгами (изначально 0 денег).
#
# Если сытость человека становится меньше нуля, человек умирает.
#
# Логика действий человека определяется следующим образом:
#     Генерируется число кубика от 1 до 6.
#     Если сытость < 20, то нужно поесть.
#     Иначе, если еды в доме < 10, то сходить в магазин.
#     Иначе, если денег в доме < 50, то работать.
#     Иначе, если кубик равен 1, то работать.
#     Иначе, если кубик равен 2, то поесть.
#     Иначе играть.
#
# По такой логике эксперимента человеку надо прожить 365 дней.
#
# Реализуйте такую программу и создайте двух людей, живущих в одном доме.
# Проверьте работу программы несколько раз.

import random


class House:

    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money

    def has_food(self):
        return self.food > 0

    def take_food(self):
        if self.has_food():
            self.food -= 1
            return True
        return False

    def add_food(self):
        self.food += 1

    def has_money(self):
        return self.money > 0

    def take_money(self):
        if self.has_money():
            self.money -= 1
            return True
        return False

    def add_money(self):
        self.money += 1


class Person:

    def __init__(self, name, house, satiety=50):
        self.name = name
        self.satiety = satiety
        self.house = house

    def is_alive(self):
        return self.satiety >= 0

    def eat(self):
        if self.house.take_food():
            self.satiety += 1
            print(f"{self.name} поел. Сытость: {self.satiety}")

    def work(self):
        self.house.add_money()
        self.satiety -= 1
        print(
            f"{self.name} поработал. Сытость: {self.satiety}, Деньги в доме: {self.house.money}"
        )

    def play(self):
        self.satiety -= 1
        print(f"{self.name} поиграл. Сытость: {self.satiety}")

    def go_shopping(self):
        if self.house.take_money():
            self.house.add_food()
            print(
                f"{self.name} сходил в магазин. Еда в доме: {self.house.food}")

    def live_one_day(self):
        dice_roll = random.randint(1, 6)

        if self.satiety < 20 or dice_roll == 2:
            self.eat()
        elif self.house.food < 10:
            self.go_shopping()
        elif self.house.money < 50 or dice_roll == 1:
            self.work()
        else:
            self.play()

        if not self.is_alive():
            print(f"{self.name} умер.")
            exit()


def live_in_one_house_365_days(*args):
    family = [*args]

    for day in range(1, 366):
        for person in family:
            if person.is_alive():
                print(f"\nДень {day}")
                person.live_one_day()
            else:
                print(f'{person.name} умер.')
                family.remove(person)

        if len(family) == 0:
            print(f'Все жители дома погибли на {day+1} день.')
            break

    if len(family) > 0:
        print(
            'Поздравляем! В доме остались выжившие. Имена этих счастливчиков: '
        )
        for person in family:
            print(person.name)


house = House()
person1 = Person("Артём", house)
person2 = Person("Наталья", house)

live_in_one_house_365_days(person1, person2)

print()
