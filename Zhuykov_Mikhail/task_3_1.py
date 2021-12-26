def num_translate(number_by_word):
    """
    Функция переводит число с английского языка на русский в диапазоне от 0 до 10
    """
    list_translate = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                      'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
                      }  # Создание словаря
    print(list_translate.get(number_by_word))


number = input('Введите словом число на английском языке от 0 до 10: ')  # Получение данных для перевода от пользователя
num_translate(number)  # Вызов функции num_translate
