price_list = [23.23, 35.8, 285.07, 2948.1, 3243.89, 91.00, 72.10, 82, 829.6, 616.90, 82.46, 9011.22, 82, 2325]
print(f'Адрес в памяти созданного списка : {id(price_list)}')
for i in price_list:  # Цикл для прохода по списку
    ruble = int(i)  # Запись количества рублей в переменную.
    cent = int(float(f'{(i % 1):.2f}') * 100)  # Вычисление целого числа из дробной части
    print(f'{ruble} руб {cent:02d} коп ', end="")  # Вывод списка цен в один ряд.

print()  # Для разделения
print(f'Адрес в памяти отредактированного списка : {id(price_list)}')

print('_________Задание В_________')
price_list.sort()  # Сортировка списка по возрастанию (задание В).
print(price_list)
print(f'Адрес в памяти отсортированного списка по возрастанию: {id(price_list)}')

print('_________Задание С_________')
descending_price_list = price_list.copy()  # Задание В. Создание нового списка.
descending_price_list.sort(reverse=True)  # Сортировка по убыванию.
print(descending_price_list)

print('_________Задание D_________')
print(descending_price_list[4::-1])
