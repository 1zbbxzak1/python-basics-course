print('Задача 7. Матрицы')

# Вы стажируетесь в лаборатории искусственного интеллекта, в ней вам поручили разработать класс Matrix
# для обработки и анализа данных. Ваш класс должен предоставлять функциональность для выполнения основных
# операций с матрицами, таких как сложение, вычитание, умножение и транспонирование.
# Это будет полезно для обработки и структурирования больших объёмов данных, которые используются в обучении нейронных сетей.
#
# Задача
# Создайте класс Matrix для работы с матрицами.
# Реализуйте методы:
#     сложения,
#     вычитания,
#     умножения,
#     транспонирования матрицы.
# Создайте несколько экземпляров класса Matrix и протестируйте реализованные операции.


class Matrix:

    def __init__(self, rows, cols, elements=None):
        self.rows = rows
        self.cols = cols
        if elements is None:
            self.elements = [[0] * cols for _ in range(rows)]
        else:
            if len(elements) != rows or any(
                    len(row) != cols for row in elements):
                raise ValueError("Недопустимые размеры матрицы")
            self.elements = elements

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.elements])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матрицы не совпадают для сложения")
        result = [[
            self.elements[i][j] + other.elements[i][j]
            for j in range(self.cols)
        ] for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матрицы не совпадают для вычитания")
        result = [[
            self.elements[i][j] - other.elements[i][j]
            for j in range(self.cols)
        ] for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError(
                    "Недопустимые размеры матрицы для умножения")
            result = [[
                sum(self.elements[i][k] * other.elements[k][j]
                    for k in range(self.cols)) for j in range(other.cols)
            ] for i in range(self.rows)]
            return Matrix(self.rows, other.cols, result)
        elif isinstance(other, (int, float)):
            result = [[self.elements[i][j] * other for j in range(self.cols)]
                      for i in range(self.rows)]
            return Matrix(self.rows, self.cols, result)
        else:
            raise ValueError("Неподдерживаемый тип операнда для умножения")

    def transpose(self):
        result = [[self.elements[j][i] for j in range(self.rows)]
                  for i in range(self.cols)]
        return Matrix(self.cols, self.rows, result)


# Пример использования
matrix1 = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix(2, 3, [[7, 8, 9], [10, 11, 12]])

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nMatrix 1 + Matrix 2:")
print(matrix1 + matrix2)

print("\nMatrix 1 - Matrix 2:")
print(matrix1 - matrix2)

matrix3 = Matrix(3, 2, [[1, 2], [3, 4], [5, 6]])
print("\nMatrix 3:")
print(matrix3)

print("\nMatrix 1 * Matrix 3 (Умножение матриц):")
print(matrix1 * matrix3)

print("\nТранспонирование матрицы 1:")
print(matrix1.transpose())