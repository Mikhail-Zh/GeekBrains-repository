def thesaurus(*names, sorting=False, sorting_direction=False):
    """
    Функция принимает список и возвращает словарь. Ключ - первая буква имени. Значение - имя.
    Именованные аргументы:
    sorting - для сортировки словаря по ключам (True - отсортировать, False - не сортировать)
    sorting_direction - сортировка по убыванию или возрастанию (True - по убыванию, False по возрастанию)
    """
    catalog_name = {}  # Создание пустого каталога
    for i in names:  # Цикл для перебора списка с именами
        if not i[0] in catalog_name:  # Если нет ключа в словаре
            catalog_name.setdefault(i[0], [i])  # Добавление ключа и значения в каталог
        else:
            catalog_name[i[0]].append(i)  # Добавление значения в каталог по ключу
    list_key = [key for key in catalog_name]  # лист ключей словаря
    list_key_s = sorted(list_key, reverse=sorting_direction)  # сортировка ключей словаря
    catalog_name_s = ({letter: catalog_name[letter] for letter in list_key_s if
                       letter in catalog_name})  # Создание словаря в зависимости от list_key_s
    return catalog_name_s if sorting else catalog_name  # Возвращение словаря в зависимости от параметра sorting


print(thesaurus("Михаил", "Светлана", "Анастасия", "Олег", "Максим", "Людмила", "Остап", "Михаил",
                sorting=True,
                sorting_direction=True
                ))  # Свой пример

print(thesaurus("Иван", "Мария", "Петр", "Илья",
                sorting=True,
                sorting_direction=False
                ))  # Свой пример
