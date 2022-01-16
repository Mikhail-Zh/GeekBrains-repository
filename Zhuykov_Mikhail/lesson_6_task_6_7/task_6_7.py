def editing_data(num_str, val):
    """
    Функция редактирует значение в файле bakery.csv.
    Принимаемые параметры:
    num_str - номер строки которую требуется отредактировать.
    val - значение, которое требуется записать.
    """
    with open('bakery.csv', 'r+', encoding='utf-8') as f:  # Открытие файла.
        count = sum(1 for _ in f)  # Счетчик строк в файле.
        if num_str <= count:  # Условие если num_str меньше числа строк в файле.
            f.seek(0)
            n = 1
            while True:  # Цикл для нахождения нужной строки.
                f.readline()  # Чтение строки.
                n += 1
                if num_str == 1:  # Условие если требуется переписать первую строку.
                    f.seek(0)
                    f.write(f'{val:<10}\n')
                    break
                elif n == num_str:
                    f.seek(f.tell())
                    f.write(f'{val:<10}\n')
                    break
        else:  # Условие если num_str больше числа строк в файле.
            print(f'Введено большое значение количества записей. На данный момент их: {count}')


if __name__ == '__main__':
    editing_data(1, '24565.39')
