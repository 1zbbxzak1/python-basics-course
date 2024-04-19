print('Задача 3. Регистрация')

# У вас есть файл с протоколом регистрации пользователей на сайте — registrations.txt.
# Каждая строка содержит имя, имейл и возраст, разделённые пробелами. Например: Василий test@test.ru 27.
#
# Напишите программу, которая проверяет данные из файла для каждой строки:
#           Присутствуют все три поля.
#           Поле «Имя» содержит только буквы.
#           Поле «Имейл» содержит @ и точку.
#           Поле «Возраст» представляет число от 10 до 99.
#
# В результате проверки сформируйте два файла:
#           registrations_good.log для правильных данных; записывать строки как есть;
#           registrations_bad.log — для ошибочных; записывать строку и вид ошибки.
#
# Для валидации строки данных напишите функцию, которая может выдавать исключения:
#           НЕ присутствуют все три поля: IndexError.
#           Поле «Имя» содержит НЕ только буквы: NameError.
#           Поле «Имейл» НЕ содержит @ и точку: SyntaxError.
#           Поле «Возраст» НЕ представляет число от 10 до 99: ValueError.

try:
    with open('registrations.txt', 'r', encoding='UTF-8') as registrations, \
         open('registrations_good.log', 'w', encoding='UTF-8') as good_log, \
         open('registrations_bad.log', 'w', encoding='UTF-8') as bad_log:

        clients = registrations.read().split('\n')

        for client in clients:
            try:
                fields = client.split()

                if len(fields) != 3:
                    raise IndexError()

                if not fields[0].isalpha():
                    raise NameError()

                if '@' not in fields[1] or '.' not in fields[1]:
                    raise SyntaxError()

                age = int(fields[2])
                if not 10 < age < 99:
                    raise ValueError()

                good_log.write(f'{client}\n')

            except IndexError:
                bad_log.write(f'{client}\tНЕ присутствуют все три поля\n')

            except NameError:
                bad_log.write(
                    f'{client}\tПоле «Имя» содержит НЕ только буквы\n')

            except SyntaxError:
                bad_log.write(
                    f'{client}\tПоле «Имейл» НЕ содержит @ и точку\n')

            except ValueError:
                bad_log.write(
                    f'{client}\tПоле «Возраст» НЕ представляет число от 10 до 99\n'
                )

except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")

print()
