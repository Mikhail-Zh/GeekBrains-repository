class MyClassException(Exception):
    pass


def func_division(a, b):
    """Функция получает два числа и первое делит на второе"""
    try:
        a = float(a)  # Перевод строкового значения в число с плавающей точкой.
        b = float(b)  # Перевод строкового значения в число с плавающей точкой.
        if b == 0:  # Если b = 0 поднимается ошибка.
            raise MyClassException('Деление на 0 не допустимо')
    except ValueError:  # Ошибка если значение не число.
        return f'Одно или оба значения не являются числом'
    except MyClassException as err:  # Ошибка если b = 0.
        return err
    else:
        return f'Частное: {a / b}'


num_1 = input('Введите делимое: ')
num_2 = input('Введите делитель: ')
print(func_division(num_1, num_2))
