import sys

with open(sys.argv[1], 'r', encoding='utf-8') as users:
    with open(sys.argv[2], 'r', encoding='utf-8') as hobby:
        with open(sys.argv[3], 'w+', encoding='utf-8') as users_hobby:
            while True:
                row_u = users.readline()  # Чтение строки из файла списка пользователей.
                row_h = hobby.readline()  # Чтение строки из файла списка хобби.
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
