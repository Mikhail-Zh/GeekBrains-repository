import sys
import json

with open('users.csv', 'r', encoding='utf-8') as u:  # Открытие файла с ФИО пользователей
    content_users = u.read().splitlines()  # Перевод текста в список
    with open('hobby.csv', 'r', encoding='utf-8') as h:  # Открытие файла с хобби пользователей
        content_hobby = h.read().splitlines()  # Перевод текста в список
    users_hobby = dict()  # Определение словаря
    for i in range(len(content_users)):  # Цикл для формирования записи и запись в файл
        if i == (len(content_users) - 1) and len(content_users) < len(content_hobby):  # Если длина списка
            # пользователей, меньше длины списка хобби.
            users_hobby[content_users[i]] = content_hobby[i]
            with open('users_hobby.json', 'w', encoding='utf-8') as f:  # Открытие файла. Если не сущ., то создастся.
                json.dump(users_hobby, f)  # Запись данных в файл.
            sys.exit(1)  # Выход с кодом 1 Если в списке нет больше пользователей, а в списке хобби есть еще данные.
        if i < len(content_hobby):  # Если строка в списке пользователей есть и в списке хобби есть
            users_hobby[content_users[i]] = content_hobby[i]  # Запись в словарь
            with open('users_hobby.json', 'w', encoding='utf-8') as f:  # Открытие файла. Если не сущ., то создастся.
                json.dump(users_hobby, f)  # Запись данных в файл.
        elif i > (len(content_hobby) - 1):  # Если строка в списке пользователей есть, а в списке хобби нет
            users_hobby[content_users[i]] = 'None'  # Запись в словарь
            with open('users_hobby.json', 'w', encoding='utf-8') as f:  # Открытие файла. Если не сущ., то создастся.
                json.dump(users_hobby, f)  # Запись данных в файл.
