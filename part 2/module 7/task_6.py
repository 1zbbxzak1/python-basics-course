print('Задача 6. Контакты — 3')

# Мы уже помогали Степану с реализацией телефонной книги на устройстве, однако внезапно оказалось,
# что ей не хватает ещё одной полезной функции — поиска.
#
# Напишите программу, которая бесконечно запрашивает у пользователя действие, которое он хочет совершить:
# добавить контакт или найти человека в списке контактов по фамилии.
#
# Действие «добавить контакт»: программа запрашивает имя и фамилию контакта,
# затем номер телефона, добавляет их в словарь и выводит на экран текущий словарь контактов.
# Если этот человек уже есть в словаре, то выводится соответствующее сообщение.
#
# Действие «поиск человека по фамилии»: программа запрашивает фамилию и выводит все контакты с такой фамилией
# и их номера телефонов. Поиск не должен зависеть от регистра символов.


def add_contact(contacts):
    full_name = tuple(
        input(
            "Введите имя и фамилию нового контакта (через пробел): ").split())

    if full_name not in contacts:
        phone_number = input("Введите номер телефона: ")
        contacts[full_name] = phone_number
    else:
        print("Такой человек уже есть в контактах.")

    print("Текущий словарь контактов:", contacts)


def search_contact(contacts):
    search_surname = input("Введите фамилию для поиска: ").lower()
    matching_contacts = [(name.capitalize(), surname.capitalize(), phone)
                         for (name, surname), phone in contacts.items()
                         if surname.lower() == search_surname]

    if matching_contacts:
        for name, surname, phone in matching_contacts:
            print(f"{name} {surname}: {phone}")
    else:
        print("Контакты с такой фамилией не найдены.")


def main():
    contacts = {}

    while True:
        print("\nВведите номер действия:")
        print("1. Добавить контакт")
        print("2. Найти человека")
        print("3. Выйти")

        choice = input("При выборе действия (1, 2 или 3): ")

        if choice == '1':
            add_contact(contacts)

        elif choice == '2':
            search_contact(contacts)

        elif choice == '3':
            print('Программа завершена')
            break

        else:
            print("Некорректный ввод. Пожалуйста, введите 1, 2 или 3.")


main()

print()
