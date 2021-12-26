def num_translate_adv(number_by_word: str):
    """
    Функция переводит число с английского языка на русский в диапазоне от 0 до 10
    """
    list_translate = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                      'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
                      }  # Создание словаря
    if number_by_word.istitle():  # Проверяется условие если первая буква заглавная
        print((list_translate.get(number_by_word.lower())).title())  # Печать с заглавной буквы
    else:
        print(list_translate.get(number_by_word))


number = input('Введите словом число на английском языке от 0 до 10: ')  # Получение от пользователя данных для перевода
num_translate_adv(number)  # Вызов функции num_translate
