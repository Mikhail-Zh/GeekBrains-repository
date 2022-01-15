import sys
import json

with open('users.csv', 'r', encoding='utf-8') as u:
    content_users = u.read().splitlines()
    with open('hobby.csv', 'r', encoding='utf-8') as h:
        content_hobby = h.read().splitlines()
    users_hobby = dict()
    for i in range(len(content_users)):
        if i == (len(content_users) - 1) and len(content_users) < len(content_hobby):
            users_hobby[content_users[i]] = content_hobby[i]
            with open('users_hobby.json', 'w', encoding='utf-8') as f:
                json.dump(users_hobby, f)
            sys.exit(1)
        if i < len(content_hobby):
            users_hobby[content_users[i]] = content_hobby[i]
        elif i > (len(content_hobby) - 1):
            users_hobby[content_users[i]] = 'None'
