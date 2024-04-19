print('Задача 1. Драка')

# Вы работаете в команде разработчиков мобильной игры, и вам досталась часть от ТЗ заказчика.
#
# Есть два юнита, каждый называется «Воин». Каждому устанавливается здоровье в 100 очков.
# Они бьют друг друга в случайном порядке. Тот, кто бьёт, здоровье не теряет.
# У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение, какой юнит атаковал и сколько у противника осталось здоровья.
# Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.

import random


class Warrior:

    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def attack(self, opponent):
        damage = 20
        print(
            f"{self.name} атакует {opponent.name}! {opponent.name} теряет {damage} здоровья."
        )
        opponent.health -= damage
        if opponent.health <= 0:
            print(f"{opponent.name} выбывает из боя!")
            print(f"{self.name} побеждает!")


def battle(warrior1, warrior2):
    while warrior1.health > 0 and warrior2.health > 0:
        attacker = random.choice([warrior1, warrior2])
        opponent = warrior2 if attacker == warrior1 else warrior1
        attacker.attack(opponent)
        print(
            f"{warrior1.name}: {warrior1.health} здоровья, {warrior2.name}: {warrior2.health} здоровья."
        )


warrior1 = Warrior("Воин 1")
warrior2 = Warrior("Воин 2")

print("Начинается битва!")
battle(warrior1, warrior2)

print()