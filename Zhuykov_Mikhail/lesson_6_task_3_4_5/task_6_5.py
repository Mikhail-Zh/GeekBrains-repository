import sys

with open(sys.argv[1], 'r', encoding='utf-8') as users:
    with open(sys.argv[2], 'r', encoding='utf-8') as hobby:
        with open(sys.argv[3], 'w+', encoding='utf-8') as users_hobby:
            while True:
                row_u = users.readline()
                row_h = hobby.readline()
                if row_u and row_h:
                    users_hobby.write(f'{row_u.strip()}: {row_h.strip()}\n')
                elif row_u and not row_h:
                    users_hobby.write(f'{row_u.strip()}: None\n')
                elif not row_u and row_h:
                    sys.exit(1)
                else:
                    break
