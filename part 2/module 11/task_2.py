print('Задача 2. Студенты')

# Реализуйте модель с именем Student,
# содержащую поля «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
# Затем создайте список из десяти студентов
# (данные о студентах можете придумать или запросить у пользователя)
# и отсортируйте список по возрастанию среднего балла. Выведите результат на экран.


class Student:

    def __init__(self, id, full_name, group_number, grades):
        self.id = id
        self.full_name = full_name
        self.group_number = group_number
        self.grades = grades

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)


# Реализация ввода данных
# def input_student_data():
#     full_name = input("Введите ФИ студента: ")
#     group_number = input("Введите номер группы: ")

#     grades = []
#     for i in range(5):
#         grade = float(input(f"Введите оценку {i + 1}: "))
#         grades.append(grade)

#     return Student(full_name, group_number, grades)

# students = []

# for _ in range(10):
#     student = input_student_data()
#     students.append(student)

# Пример ввода данных
students: list[Student] = [
    Student(1, 'Edward Johnson', 1, [5, 5, 4, 1, 2]),
    Student(2, 'Raymond Edwards', 1, [4, 4, 2, 2, 5]),
    Student(3, 'Milton Hawkins', 1, [3, 4, 3, 4, 4]),
    Student(4, 'Joseph Reynolds', 1, [2, 4, 3, 2, 5]),
    Student(5, 'Anthony Floyd', 2, [3, 4, 5, 2, 1]),
    Student(6, 'Albert Abbott', 2, [5, 2, 3, 2, 1]),
    Student(7, 'Darrell Rodriguez', 2, [4, 4, 5, 3, 5]),
    Student(8, 'Glenn Welch', 2, [1, 4, 3, 5, 5]),
    Student(9, 'Michael Reynolds', 3, [4, 5, 3, 2, 1]),
    Student(10, 'Mark Day', 3, [4, 2, 3, 5, 5])
]

students_sorted = sorted(students, key=lambda x: x.get_average_grade())

print("\nСписок студентов, отсортированный по среднему баллу:")
for student in students_sorted:
    print(
        f"ФИ: {student.full_name}, Группа: {student.group_number}, Средний балл: {student.get_average_grade()}"
    )

print()
