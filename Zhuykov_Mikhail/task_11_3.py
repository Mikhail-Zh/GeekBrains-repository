class MyClassException(Exception):
    pass


def list_numbers():
    """Функция принимает данные от пользователя. Если это число добавляет в список"""
    lst_num = []  # Список для хранения чисел введенных пользователем
    el_enter = True  # Объявление переменной. True для того, чтобы войти в цикл.
    while el_enter:
        el_enter = input('Введите данные или наберите команду stop для прекращения работы: ')
        try:
            if el_enter.isdigit() is False and el_enter != 'stop':  # Если данные состоят не из цифр - поднять ошибку
                raise MyClassException('Данные должны содержать только числовые значения.')
            elif el_enter == 'stop':  # Если введена команда stop
                return lst_num
        except MyClassException as err:
            print(err)
        else:
            lst_num.append(int(el_enter))  # Если ошибок не было добавить элемент в список


print(list_numbers())
