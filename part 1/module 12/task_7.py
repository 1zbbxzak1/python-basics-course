print('Задача 7. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
#
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
#
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
#
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
#
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
#
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
#
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.

import random

def rock_paper_scissors():
    print('Запущена игра: Камень, ножницы, бумага.')
    print('1. Камень')
    print('2. Ножницы')
    print('3. Бумага')
    while True:
        pl_move = int(input('Ваш ход (1 , 2, 3): '))
        ii_move = random.randint(1, 3)
        if (pl_move, ii_move) in ((1, 1), (2, 2), (3, 3)):
            print('Ничья.')
        elif (pl_move, ii_move) in ((1, 2), (2, 3), (3, 1)):
            print('Игрок выиграл.')
        else:
            print('ИИ выиграл.')
        reload = input('Перезапустить (y, n): ')
        if reload == 'n':
            break

def guess_the_number():
    print('Запущена игра: Угадай число.')
    ran_int = random.randint(1, 10)
    print('Загадано целое число от 1 до 10.')
    while True:
        ans_user = int('Введите число: ')
        if ans_user == ran_int:
            print('Поздравляем! Вы отгадали число.')
            break
        print('Неверно. Попробуйте еще раз.')

def mainMenu():
    print('Выберите игру (1, 2):')
    print('1. Камень, ножницы, бумага')
    print('2. Угадай число')

    choice = input('Ваш выбор: ')
    if choice == '1':
        rock_paper_scissors()
    elif choice == '2':
        guess_the_number()
    else:
        print('Неверное действие. Попробуйте ещё раз.')

mainMenu()
