print('Задача 6. Быстрая сортировка')

# Реализуйте алгоритм быстрой сортировки (её называют сортировкой Хоара).
#
# За один шаг алгоритма выполните следующие действия:
#
# Выберите один элемент списка (его иногда называют опорным элементом).
# Сделать это можно разными способами, но важно придерживаться одного принципа.
# В нашем случае опорным элементом всегда будет крайний правый (например, в списке [1, 2, 3] это 3).

# Разбейте текущий список на три части: элементы меньше опорного, равные опорному и больше опорного.
# В списке [5, 8, 9, 4, 2, 9, 1, 8] опорным элементом будет число 8 (крайнее правое), а получить надо три списка:
# [5, 4, 2, 1];
# [8, 8];
# [9, 9].

# Для списка с элементами меньше опорного ([5, 4, 2, 1]) и списка с элементами больше опорного ([9, 9]) выполните
# те же шаги заново — запустите рекурсию.
# результат_1 = рекурсия([5, 4, 2, 1]).
# результат_2 = [8, 8].
# результат_3 = рекурсия([9, 9]).

# Сложите результаты вызова рекурсий и получите отсортированный список:
# отсортированный_список = результат_1 + результат_2 + результат_3.


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    less = []
    equal = []
    greater = []

    for num in arr:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)

    return quicksort(less) + equal + quicksort(greater)


unsorted_list = [5, 8, 9, 4, 2, 9, 1, 8]
sorted_list = quicksort(unsorted_list)

print("Отсортированный список:", sorted_list)
