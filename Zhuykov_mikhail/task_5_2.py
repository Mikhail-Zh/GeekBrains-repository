from itertools import islice
from sys import getsizeof


def odd_num_gen(n):
    """
    Функция генератора нечетных чисел от 1 до 'n' включительно.
    """
    return (num for num in range(1, n + 1, 2))


odd_num = odd_num_gen(79)
print(type(odd_num), getsizeof(odd_num))  # Определение типа и занимаемого места в памяти.
print(next(odd_num))  # Получение первого значения генератора
print(next(odd_num))  # Получение второго значения генератора
print(next(odd_num))  # Получение третьего значения генератора
print(next(odd_num))  # Получение четвертого значения генератора
print(*islice(odd_num, 6))  # Срез. Получение шести значений генератора от последнего полученного.
print(*odd_num)  # Получение остальных значений генератора.
