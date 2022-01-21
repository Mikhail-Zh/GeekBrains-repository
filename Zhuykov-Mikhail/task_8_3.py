def type_logger(func):  # Декоратор
    def logger(*args, **kwargs):
        """
        Принимает аргументы для функции calc_cube и возвращает данные по каждому аргументу: имя функции,
        принятый аргумент, тип принятого аргумента.
        Реализован прием позиционных и именованных аргументов, чтобы принимать больше аргументов, чем предусмотрено
        функцией calc_cube.
        """
        list_num_val = []  # Определение пустого списка для хранения значений позиционных и именованных аргументов.
        if args:  # Если есть позиционные аргументы добавить в список.
            [list_num_val.append(i) for i in args]
        if kwargs:  # Если есть именованные аргументы добавить в список.
            [list_num_val.append(val) for val in kwargs.values()]
        cube = map(func, list_num_val)  # Применение функции calc_cube к каждому полученному аргументу.
        cube = [*cube]  # Распаковка данных полученных функцией map()
        count = 0  # Счетчик
        cube_list = []  # Определение пустого списка для хранения данных полученных аргументов.
        for _ in map(func, list_num_val):
            cube_list.append(f'{func.__name__}'  # Имя функции
                             f'({list_num_val[count]}: '  # Значение полученного аргумента
                             f'{type(list_num_val[count])})')  # Тип значения функции
            count += 1
        print(*cube_list, sep=', ')  # Вывод данных полученных аргументов через запятую.
        return cube
    return logger


@type_logger
def calc_cube(x):
    """
    Функция получения куба полученного числа.
    """
    return x ** 3


cube_num = calc_cube(1, 2, 3, x=4, y=5)
print(cube_num, sep=', ')
