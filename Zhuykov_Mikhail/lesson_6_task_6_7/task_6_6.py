def read_data(start=0, stop=0):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        n = 0
        for row in f:
            n += 1
            if start == 0 and stop == 0:
                print(row.strip())
            elif start <= n and stop == 0:
                print(row.strip())
            elif start == 0 and stop >= n:
                print(row.strip())
            elif start <= n <= stop:
                print(row.strip())
            elif start > stop:
                print("Запрашиваемая начальная позиция списка не может быть больше конечной позиции")
                break
            if n == stop:
                break


def data_record(sales_amount):
    with open('bakery.csv', 'a+', encoding='utf-8') as f:
        f.write(f'{sales_amount}\n')


if __name__ == '__main__':
    data_record(525)
    read_data(2, 8)
