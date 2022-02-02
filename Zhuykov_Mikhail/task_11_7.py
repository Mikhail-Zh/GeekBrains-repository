class ComplexNumber:  # Класс создает комплексное число
    def __init__(self, a, b):  # Инициализатор.
        self.complex_num = complex(a, b)  # Создание комплексного числа.

    def __add__(self, other):  # Перегрузка. Сложение комплексных чисел.
        return self.complex_num + other.complex_num

    def __mul__(self, other):  # Перегрузка. Умножение комплексных чисел.
        return self.complex_num * other.complex_num


complex_num_1 = ComplexNumber(3, 5)  # Создание первого экземпляра класса
print(complex_num_1.complex_num)

complex_num_2 = ComplexNumber(10, -6)  # Создание второго экземпляра класса
print(complex_num_2.complex_num)

complex_num_3 = ComplexNumber(0, -3)  # Создание третьего экземпляра класса
print(complex_num_3.complex_num)

print(complex_num_1 + complex_num_2)  # Сложение первого и второго экземпляра класса
print(complex_num_1 * complex_num_2)  # Умножение первого и второго экземпляра класса
print(complex_num_1 * complex_num_3)  # Умножение первого и третьего экземпляра класса
