import task_6_1


def spam_request(req_list):
    """
    Функция определяет максимальное количество запросов и с какого адреса они произведены.
    """
    request_max = dict()  # Определение словаря. Будет хранить в себе данные в виде: адрес запроса и количество запросов
    for el in req_list:  # Цикл для подсчета количества полученных запросов с каждого адреса.
        if el[0] not in request_max:  # Если в словаре нет, то добавить со значением 1.
            request_max[el[0]] = 1
        else:  # Иначе добавить к значению 1.
            request_max[el[0]] = request_max[el[0]] + 1
    max_spam = 0  # Определение переменной для хранения максимального количества запросов.
    max_spam_temp = dict()  # Для хранения адреса и количества запросов с максимальным количеством запросов.
    for key, val in request_max.items():  # Цикл для определения самого большого количества запросов.
        if val == max_spam:  # Если значение равно значению в переменной max_spam..
            max_spam_temp[key] = val  # Добавить данные в словарь.
        elif val > max_spam:  # Если значение больше значению в переменной max_spam.
            max_spam = val  # Присвоить переменной max_spam новое значение.
            max_spam_temp.clear()  # Очистить словарь max_spam_temp.
            max_spam_temp[key] = val  # Добавить новые данные в словарь.
        else:  # Иначе продолжить цикл
            continue
    return (f'Самое большое количество запросов - {v} шт., c IP адреса: {k}' for k, v in max_spam_temp.items())


print(*spam_request(task_6_1.request_logs()))
