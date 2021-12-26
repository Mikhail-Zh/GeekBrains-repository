from random import choice


def get_jokes(n=1, flag='no'):
    """
    Функция возвращает список шуток составленный из слов списков nouns, adverbs, adjectives.
    Именованные параметры:
    n - задает количество шуток в списке (по умолчанию 1). Если заданное значение n больше длины самого короткого
    списка, n присваивается значение длины самого короткого списка.
    flag - флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово в шутках можно использовать
    только один раз). 'no' - повторы разрешены. 'yes' - повторы запрещены (по умолчанию n=1, flag='no').
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["весёлый", "яркий", "зелёный", "утопичный", "мягкий"]
    list_jokes = []
    min_list_length = min(len(nouns), len(adverbs), len(adjectives))  # Определение минимальной длины списков
    n = (min_list_length if n > min_list_length and flag == 'yes' else n)  # Определение нужного диапазона для n
    for _ in range(n):
        if flag == 'no':  # Если разрешен повтор слов в шутках
            list_jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        elif flag == 'yes':  # Если запрещен повтор слов в шутках
            nouns_i = choice(nouns)
            adverbs_i = choice(adverbs)
            adjectives_i = choice(adjectives)
            nouns.remove(nouns_i)
            adverbs.remove(adverbs_i)
            adjectives.remove(adjectives_i)
            list_jokes.append(f'{nouns_i} {adverbs_i} {adjectives_i}')
    return list_jokes


print(get_jokes(flag='yes', n=4))
