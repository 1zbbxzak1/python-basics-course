print('Задача 5. Стек')

# Мы уже говорили, что в программировании нередко необходимо создавать свои собственные
# структуры данных на основе уже существующих. Одной из таких базовых структур является стек.
#
# Стек — это абстрактный тип данных, представляющий собой список элементов,
# организованных по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»).
#
# Простой пример: стек из книг на столе. Единственной книгой, обложка которой видна, является самая верхняя.
# Чтобы получить доступ, например, к третьей снизу книге, нам нужно убрать все книги, лежащие сверху, одну за другой.
#
# Напишите класс, который реализует стек и его возможности (достаточно будет добавления и удаления элемента).
#
# После этого напишите ещё один класс — «Менеджер задач». В менеджере задач можно выполнить команду «новая задача»,
# в которую передаётся сама задача (str) и её приоритет (int). Сам менеджер работает на основе стека (не наследование).
# При выводе менеджера в консоль все задачи должны быть отсортированы
# по следующему приоритету: чем меньше число, тем выше задача.
#
# Вот пример основной программы:
# manager = TaskManager()
# manager.new_task("сделать уборку", 4)
# manager.new_task("помыть посуду", 4)
# manager.new_task("отдохнуть", 1)
# manager.new_task("поесть", 2)
# manager.new_task("сдать ДЗ", 2)
# print(manager)
#
# Результат:
# 1 — отдохнуть
# 2 — поесть; сдать ДЗ
# 4 — сделать уборку; помыть посуду
#
# Дополнительно: реализуйте также удаление задач и подумайте, что делать с дубликатами.


class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


class TaskManager:

    def __init__(self):
        self.tasks = Stack()

    def new_task(self, task, priority):
        self.tasks.push((task, priority))
        self.sort_tasks()

    def remove_task(self, task):
        updated_tasks = Stack()
        while not self.tasks.is_empty():
            current_task = self.tasks.pop()
            if current_task[0] != task:
                updated_tasks.push(current_task)

        while not updated_tasks.is_empty():
            self.tasks.push(updated_tasks.pop())

    def sort_tasks(self):
        sorted_tasks = sorted(self.tasks.items,
                              key=lambda x: x[1],
                              reverse=True)
        self.tasks.items = sorted_tasks

    def __str__(self):
        result = ""
        current_priority = None
        for task, priority in reversed(self.tasks.items):
            if priority != current_priority:
                if current_priority is not None:
                    result += "\n"
                result += f"{priority} — {task}"
                current_priority = priority
            else:
                result += f"; {task}"
        return result


# Пример использования:
manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)
print(manager)

# Удаление задачи
manager.remove_task("помыть посуду")
print("\nПосле удаления задачи 'помыть посуду':")
print(manager)

print()
