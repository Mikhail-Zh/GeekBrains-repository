def editing_data(num_str, val):
    with open('bakery.csv', 'r+', encoding='utf-8') as f:
        count = sum(1 for _ in f)
        if num_str <= count:
            f.seek(0)
            n = 1
            while True:
                f.readline()
                n += 1
                if num_str == 1:
                    f.seek(0)
                    f.write(f'{val:<10}\n')
                    break
                elif n == num_str:
                    f.seek(f.tell())
                    f.write(f'{val:<10}\n')
                    break
        else:
            print(f'Введено большое значение количества записей. На данный момент их: {count}')


if __name__ == '__main__':
    editing_data(1, '24565.39')
