print('Задача 4. Чат')

# Реализуйте программу — чат, в котором могут участвовать сразу несколько человек,
# то есть программу, которая может работать одновременно для нескольких пользователей.
# При запуске запрашивается имя пользователя. После этого он выбирает одно из действий:
#           Посмотреть текущий текст чата.
#           Отправить сообщение (затем вводит сообщение).
# Действия запрашиваются бесконечно.
#
# Примечание: для решения задачи вам достаточно текущих знаний, нужно лишь проявить немного
# фантазии и хитрости. Не углубляйтесь в дебри работы с сетями, создание GUI-приложений и прочее.
# Однако, если очень хочется, то останавливать вас никто не будет!


def show_chat():
    try:
        with open('chat.txt', 'r', encoding='UTF-8') as chat_file:
            print("\n=== Чат ===")
            for line in chat_file:
                print(line.rstrip())
            print("===========")
    except FileNotFoundError:
        print("Чат еще не содержит сообщений.")


def send_message(user_name, message):
    with open('chat.txt', 'a', encoding='UTF-8') as chat_file:
        chat_file.write(f"{user_name}: {message}\n")
    print("Сообщение отправлено!")


def start_chat(user_name):
    while True:
        print("\nВыберите действие:")
        print("1. Посмотреть текущий текст чата.")
        print("2. Отправить сообщение.")
        print("3. Выйти из чата.")

        choice = input("Ваш выбор: ")

        if choice == '1':
            show_chat()
        elif choice == '2':
            message = input("Введите сообщение: ")
            send_message(user_name, message)
        elif choice == '3':
            print("Выход из чата. До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")


user_name = input("Введите ваше имя: ")
start_chat(user_name)

print()
