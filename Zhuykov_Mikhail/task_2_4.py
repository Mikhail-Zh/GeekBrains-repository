employee_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                 'токарь высшего разряда нИКОЛАй', 'директор аэлита'
                 ]
for i in employee_list:  # Цикл для прохода по элементам списка
    name = i.split()  # Разделение элемента списка
    name = name[-1].title()  # Редактирование имени. Первая буква большая, остальные маленькие
    print(f'Привет, {name}!')  # Вывод приветствия