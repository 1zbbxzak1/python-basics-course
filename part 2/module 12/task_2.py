print('Задача 2. Карма')

# Один буддист-программист решил создать свой симулятор жизни, в котором нужно
# набрать 500 очков кармы (это константа), чтобы достичь просветления.
#
# Каждый день вызывается специальная функция one_day(), которая возвращает количество
# кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из исключений:
#
# KillError,
# DrunkError,
# CarCrashError,
# GluttonyError,
# DepressionError.
# (Исключения нужно создать самостоятельно, при помощи наследования от Exception.)
#
# Напишите такую программу. Функцию оберните в бесконечный цикл, выход из которого возможен
# только при накоплении кармы до уровня константы. Исключения обработайте и запишите в отдельный лог karma.log.
#
# По итогу у вас может быть примерно такая структура программы:
#     открываем файл
#     цикл по набору кармы
#        try
#           карма += one_day()
#        except(ы) с указанием классов исключений, которые нужно поймать
#           добавляем запись в файл
#     закрываем файл

import random


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day():
    karma_points = random.randint(1, 7)

    # Вероятность 1 к 10
    if random.randint(1, 10) == 1:
        raise random.choice([
            KillError, DrunkError, CarCrashError, GluttonyError,
            DepressionError
        ])

    return karma_points


def main():
    karma_goal = 500
    karma = 0

    with open("karma.log", "a") as log_file:
        while karma < karma_goal:
            try:
                karma_points = one_day()
                karma += karma_points
                print(f"День: Получено {karma_points} кармы. Всего: {karma}")
            except (KillError, DrunkError, CarCrashError, GluttonyError,
                    DepressionError) as e:
                log_file.write(
                    f"День: Произошло исключение {type(e).__name__}. Карма осталась на уровне {karma}\n"
                )


main()

print()
