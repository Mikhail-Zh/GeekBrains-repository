import sys

with open('users.csv', 'r', encoding='utf-8') as u:
    with open('hobby.csv', 'r', encoding='utf-8') as h:
        with open('users_hobby.txt', 'w+', encoding='utf-8') as users_hobby:
            while True:
                row_u = u.readline()
                row_h = h.readline()
                if row_u and row_h:
                    users_hobby.write(f'{row_u.strip()}: {row_h.strip()}\n')
                elif row_u and not row_h:
                    users_hobby.write(f'{row_u.strip()}: None\n')
                elif not row_u and row_h:
                    sys.exit(1)
                else:
                    break
