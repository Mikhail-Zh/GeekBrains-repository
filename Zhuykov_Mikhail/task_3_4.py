def thesaurus_adv(*names, sorting=False, sorting_direction=False):
    """
    Функция принимает список в формате «Имя Фамилия» и возвращающую словарь,
    в котором ключи — первые буквы фамилий, а значения — словари. В них Ключ - первая буква имени, а значение -
    Имя и фамилия.
    Именованные аргументы:
    sorting - для сортировки словаря по ключам (True - отсортировать, False - не сортировать)
    sorting_direction - сортировка по убыванию или возрастанию (True - по убыванию, False по возрастанию)
    """
    catalog_lastname = {}  # Создание пустого каталога
    for i in names:  # Цикл для перебора принимаемого списка
        n = i.split(' ')  # Разделение значения "Имя Фамилия"
        if not n[1][0] in catalog_lastname:  # Если нет ключа в словаре
            catalog_lastname.setdefault(n[1][0], [i])  # Добавление ключа и значения в каталог
        else:
            catalog_lastname[n[1][0]].append(i)  # Добавление значения в каталог по ключу
    for key, val in catalog_lastname.items():
        catalog_firstname = {}
        for idx in val:
            if not idx[0] in catalog_firstname:  # Если нет ключа в словаре
                catalog_firstname.setdefault(idx[0], [idx])  # Добавление ключа и значения в каталог
            else:
                catalog_firstname[idx[0]].append(idx)  # Добавление значения в каталог по ключу
        catalog_firstname_s = sorted(catalog_firstname, reverse=sorting_direction)  # сортировка ключей имени словаря
        catalog_firstname_sort = ({letter: catalog_firstname[letter]
                                   for letter in catalog_firstname_s
                                   if letter in catalog_firstname})  # Словарь в зависимости от catalog_firstname_s
        catalog_lastname[key] = catalog_firstname_sort

    #  Сортировка по ключам фамилий
    list_key_lastname = [key for key in catalog_lastname]  # лист ключей фамилий словаря
    list_key_lastname_s = sorted(list_key_lastname, reverse=sorting_direction)  # сортировка ключей словаря
    catalog_lastname_s = ({letter: catalog_lastname[letter] for letter in list_key_lastname_s if
                           letter in catalog_lastname})  # Создание словаря в зависимости от list_key_lastname_s

    return catalog_lastname_s if sorting else catalog_lastname  # Возвращение словаря в зависимости от параметра sorting


print(thesaurus_adv("Михаил Иванов", "Светлана Сергеева", "Анастасия Макеева", "Андрей Сыроежкин", "Максим Очин",
                    "Людмила Синицына", "Игорь Сидоров",
                    sorting=False,
                    sorting_direction=False
                    ))  # Свой пример

print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева",
                    sorting=False,
                    sorting_direction=False
                    ))  # Пример из задания
