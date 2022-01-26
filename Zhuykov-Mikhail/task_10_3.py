class Cell:

    def __init__(self, num_cell):  # Инициализатор.
        self.num_cell = int(num_cell)

    def __add__(self, other):  # Переопределение __add__.
        return self.num_cell + other.num_cell

    def __sub__(self, other):  # Переопределение __sub__.
        if self.num_cell > other.num_cell:  # Если первая клетка больше второй.
            return self.num_cell - other.num_cell
        if self.num_cell <= other.num_cell:  # Если первая клетка меньше или равна второй.
            return f'Количество ячеек первой клетки должно быть больше количества ячеек второй клетки'

    def __mul__(self, other):  # Переопределение __mul__.
        return self.num_cell * other.num_cell

    def __truediv__(self, other):  # Переопределение __truediv__.
        return self.num_cell // other.num_cell

    def make_order(self, num_row_cells):
        str_cells = []  # Определение словаря для хранения данных по ячейкам клетки.
        remains_num_cell = self.num_cell  # Перевод количества ячеек в переменную для дальнейшего применения в расчетах.
        num_iter = remains_num_cell // num_row_cells  # Определение числа итераций для цикла.
        for i in range(num_iter):
            if remains_num_cell // num_row_cells != 0:
                str_cells.append("*" * num_row_cells)
                remains_num_cell -= num_row_cells
            if remains_num_cell // num_row_cells == 0 and remains_num_cell % num_row_cells != 0:
                str_cells.append("*" * (remains_num_cell % num_row_cells))
        return "\n".join(str_cells)


n = Cell(24)  # Получение экземпляра класса Cell с количеством ячеек 24
z = Cell(10)  # Получение экземпляра класса Cell с количеством ячеек 24
print(n + z)
print(n - z)
print(n * z)
print(n / z)
print(n.make_order(7))  # Отображение ячеек клетки исходя из количества ячеек в ряду
print(repr(n.make_order(7)))  # Отображение в строку ячеек клетки исходя из количества ячеек в ряду
