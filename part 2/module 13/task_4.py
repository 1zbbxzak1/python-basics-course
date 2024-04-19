print('Задача 4. Односвязный список')

# Мы продолжаем тему структур данных и алгоритмов. И в этот раз вам нужно реализовать односвязный список.
#
# Связный список — это структура данных, которая состоит из элементов, называющихся узлами.
# В узлах хранятся данные, а между собой узлы соединены связями. Связь — это ссылка на следующий или предыдущий элемент списка.
#
# В односвязном списке связь — это ссылка только на следующий элемент, то есть в нём можно передвигаться только в сторону конца списка.
# Узнать адрес предыдущего элемента, опираясь на содержимое текущего узла, невозможно.
#
# Реализуйте такую структуру данных без использования стандартных структур Python (list, dict, tuple и прочие) и дополнительных модулей.
#
# Для реализации напишите два класса: Node и LinkedList. В Node должна быть логика работы одного узла (хранение данных и указателя).
#
# Для структуры реализуйте следующие методы:
#     append — добавление элемента в конец списка;
#     get — получение элемента по индексу;
#     remove — удаление элемента по индексу.


class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node

    def get(self, index):
        current = self.head
        count = 0

        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next_node

        raise IndexError("Index out of range")

    def remove(self, index):
        if index == 0:
            if self.head:
                self.head = self.head.next_node
            else:
                raise IndexError("Index out of range")
        else:
            current = self.head
            count = 0

            while current and count < index - 1:
                current = current.next_node
                count += 1

            if current and current.next_node:
                current.next_node = current.next_node.next_node
            else:
                raise IndexError("Index out of range")

    def __str__(self):
        result = []
        current = self.head

        while current:
            result.append(current.data)
            current = current.next_node

        return " -> ".join(map(str, result))


# Пример использования:
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)

print()
