from itertools import zip_longest  # Импорт функции zip_longest


class Matrix:  # Класс матрица
    def __init__(self, param):  # Инициализатор атрибутов.
        self.param = param  # Принимаемая матрица (список списков).

    def __str__(self):
        self.matrix = []  # Определения словаря. Для вывода матрицы в удобочитаемом виде.
        for row in self.param:  # Цикл для перебора строк полученной матрицы.
            self.line = []  # Определения словаря. Для хранения строки матрицы выводимой в удобочитаемом виде.
            for i in row:  # Определение элементов строк полученной матрицы.
                self.line.append(str(f'{i:^6}'))  # f'{i:^6}') выделение места под запись числа матрицы (6 символов).
            self.matrix.append(' '.join(self.line))
        return '\n'.join(self.matrix)

    def __add__(self, other):
        self.sum_matrix = []  # Определения словаря. Для хранения новой матрицы после работы метода __add__.
        for i in zip_longest(self.param, other.param):  # Цикл для перебора строк матриц которые необходимо сложить.
            if i[0] is None or i[1] is None:  # Если матрицы разных размеров.
                return f'Матрицы должны быть одного размера'
            self.item = []
            for j in zip_longest(i[0], i[1]):  # Определение элементов строк матриц которые необходимо сложить.
                if j[0] is None or j[1] is None:  # Если матрицы разных размеров.
                    return f'Матрицы должны быть одного размера'
                self.item.append(str(j[0] + j[1]))
            self.sum_matrix.append(self.item)
        return self.sum_matrix


print('----Матрица №1----')
lst_matrix_1 = [[111, 111, 111], [2, 2, 2], [3, 3, 3]]
matrix_1 = Matrix(lst_matrix_1)
print(matrix_1)
print('----Матрица №2----')
lst_matrix_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_2 = Matrix(lst_matrix_2)
print(matrix_2)
print('----Матрица №3----')
matrix_3 = matrix_1 + matrix_2
matrix_3 = Matrix(matrix_3)
print(matrix_3)

