def read_data(start=0, stop=0):
    """
    Функция выводит данные из файла bakery.csv исходя из принимаемых данных start и stop.
    Start - строка которая должна быть первой.
    Stop - строка которая должна быть последней.
    При вызове функции без параметров выводит все данные.
    """
    with open('bakery.csv', 'r', encoding='utf-8') as f:  # Открытие файла.
        n = 0  # Определение переменной для хранения номера считанной строки.
        for row in f:  # Цикл для чтения файла по строкам. И вывода запрошенных данных.
            n += 1
            # Условия для вывода данных:
            if start == 0 and stop == 0:
                print(row.strip())
            elif start <= n and stop == 0:
                print(row.strip())
            elif start == 0 and stop >= n:
                print(row.strip())
            elif start <= n <= stop:
                print(row.strip())
            if n == stop:
                break


def data_record(sales_amount):
    """
    Функция для записи данных в файл bakery.csv
    """
    with open('bakery.csv', 'a+', encoding='utf-8') as f:
        f.write(f'{sales_amount:<10}\n')  # Запись данных в файл. <10 - размер строки под запись цены.


if __name__ == '__main__':
    data_record(4570.34)
    read_data()
