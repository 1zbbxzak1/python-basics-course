print('Задача 1. Налоги')

# Реализуйте иерархию классов, описывающих имущество налогоплательщиков.
# Она должна состоять из базового класса Property и производных от него классов Apartment, Car и CountryHouse.
#
# Базовый класс должен иметь атрибут worth (стоимость), который передаётся в конструктор,
# и метод расчёта налога, переопределённый в каждом из производных классов.
# Налог на квартиру вычисляется как 1/1000 её стоимости, на машину — 1/200, на дачу — 1/500.
#
# Каждый дочерний класс должен иметь конструктор с одним параметром,
# передающий свой параметр конструктору базового класса.
#
# Разработайте интерфейс программы. Пусть она запрашивает у пользователя количество его денег
# и стоимость имущества, а затем выдаёт налог на соответствующее имущество
# и показывает, сколько денег ему не хватает (если это так).


class Property:

    def __init__(self, worth):
        self._worth = worth

    def get_worth(self):
        return self._worth

    def set_worth(self, worth):
        self._worth = worth

    def calculate_tax(self):
        pass


class Apartment(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.get_worth() / 1000


class Car(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.get_worth() / 200


class CountryHouse(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.get_worth() / 500


def main():
    money = float(input("Введите количество ваших денег: "))
    apartment_worth = float(input("Введите стоимость вашей квартиры: "))
    car_worth = float(input("Введите стоимость вашей машины: "))
    country_house_worth = float(input("Введите стоимость вашей дачи: "))

    taxpayer_apartment = Apartment(apartment_worth)
    taxpayer_car = Car(car_worth)
    taxpayer_country_house = CountryHouse(country_house_worth)

    total_tax = taxpayer_apartment.calculate_tax(
    ) + taxpayer_car.calculate_tax() + taxpayer_country_house.calculate_tax()

    print("\nНалог на квартиру:", taxpayer_apartment.calculate_tax())
    print("Налог на машину:", taxpayer_car.calculate_tax())
    print("Налог на дачу:", taxpayer_country_house.calculate_tax())

    print("\nОбщий налог:", total_tax)

    if total_tax > money:
        print("Вам не хватает", total_tax - money, "денег для уплаты налога.")
    else:
        print("У вас достаточно денег для уплаты налога.")


main()

print()
