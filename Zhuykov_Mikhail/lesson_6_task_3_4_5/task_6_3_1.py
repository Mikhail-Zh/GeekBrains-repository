import json

with open('users_hobby.json', 'r', encoding='utf-8') as f:  # Открытие файла users_hobby.json
    fail = f.read()  # Сохранение текста файла users_hobby.json в переменную
text = json.loads(fail)  # Десериализация файла users_hobby.json
print(text)
