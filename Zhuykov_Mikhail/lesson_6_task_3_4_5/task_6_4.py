import sys

with open('users.csv', 'r', encoding='utf-8') as u:  # Открытие файла с ФИО пользователей.
    with open('hobby.csv', 'r', encoding='utf-8') as h:  # Открытие файла с хобби пользователей.
        with open('users_hobby.txt', 'w+', encoding='utf-8') as users_hobby:  # Открытие файла users_hobby.txt.
            while True:
                row_u = u.readline()  # Чтение строки из файла списка пользователей.
                row_h = h.readline()  # Чтение строки из файла списка хобби.
                if row_u and row_h \
                        and not row_u.isspace():  # Есть пользователь, хобби. Строка не состоит из управляющих символов.
                    users_hobby.write(f'{row_u.strip()}: {row_h.strip()}\n')  # Запись строки в файл.
                elif row_u and not row_h \
                        and not row_u.isspace():  # Есть пользователь, нет хобби. Не состоит из управляющих символов.
                    users_hobby.write(f'{row_u.strip()}: None\n')  # Запись строки в файл.
                elif not row_u and row_h:  # Нет пользователя, есть хобби.
                    sys.exit(1)
                else:
                    break
