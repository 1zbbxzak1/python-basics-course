print('Задача 4. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
#
# Напишите программу,
# которая получает список оценок - N чисел - и выводит на экран сообщение о том,
# кого сегодня больше: отличников, хорошистов или троечников.

# Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.

count_five = 0
count_four = 0
count_three = 0

for count_all in range(int(input('Введите количество оценок: '))):
    grade = int(input('Введите оценку: '))
    if grade == 5:
        count_five += 1
    elif grade == 4:
        count_four += 1
    elif grade == 3:
        count_three += 1

if count_five > count_four and count_five > count_three:
    print('Отличников больше')

elif count_four > count_five and count_four > count_three:
    print('Хорошистов больше')

elif count_three > count_five and count_three > count_four:
    print('Троечников больше')

elif count_five == count_four and count_five > count_three:
    print('Количество отличников и хорошистов одинаково')

elif count_five == count_three and count_five > count_four:
    print('Количество отличников и троечников одинаково')

elif count_four == count_three and count_four > count_five:
    print('Количество хорошистов и троечников одинаково')

else:
    print('Одинаково')