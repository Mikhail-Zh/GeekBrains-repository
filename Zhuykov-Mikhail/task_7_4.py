import os


def file_size_stat(items):
    """
    Функция собирает статистику по размерам файлов в каталоге и подкаталогах.
    """
    size_file_stat = {0: 0}  # Определение словаря в котором будет храниться статистика.
    for dir_path, dir_names, file_names in os.walk(items):  # Цикл для прохода по всему каталогу и подкаталогам.
        with os.scandir(dir_path) as it:  # Использование менеджера контекста для 'scandir'.
            for item in it:  # Цикл для определения размера файла в папке и добавление статистики в словарь.
                if not os.path.isfile(item):  # Условие: если не является файлом
                    continue
                n = item.stat().st_size  # Переменная для хранения значения при вычислении при делении на 10
                degree_of_num = 0  # Переменная для хранения степени числа
                for _ in range(len(str(item.stat().st_size))):  # Цикл для вычисления ключа для словаря size_file_stat
                    if item.stat().st_size == 0:  # Если размер файла равен 0 байт
                        key = 0
                    elif not 0.1 <= item.stat().st_size <= 1:  # Если размер файла не больше 0.1 и не меньше 1
                        n /= 10
                        degree_of_num += 1
                        key = 10 ** degree_of_num
                if size_file_stat.get(key) is None:  # Если в словаре нет ключа: добавляет ключ и значение = 1.
                    size_file_stat[key] = 1
                else:  # Если в словаре есть ключ: к текущему значению прибавляется 1.
                    size_file_stat[key] = size_file_stat[key] + 1
    return size_file_stat


folder = os.path.abspath('some_data')
print(file_size_stat(folder))
