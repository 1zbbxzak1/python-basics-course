print('Задача 5. Часы')

# Напишите программу,
# которая получает на вход число n — количество минут, — затем считает,
# 1) сколько это будет в часах
# 2) сколько минут останется
# и выводит на экран эти два результата.
# (В вычислениях вам помогут операции // и %)

minutes = int(input('Введите количество минут: '))
hours = minutes // 60
minutes = minutes % 60
print(
 f'После подсчета: {hours} - количество часов, {minutes} - количество оставшихся минут'
)
print()
