def request_logs():
    """
    Функция получает из файла лога nginx_logs.txt данные об адресе запроса, типу запроса и ресурс запроса.
    Данные сводит в кортеж и добавляет их в список.
    """
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:  # Открытие файла
        request_list = []  # Определение списка в котором будут храниться кортежи запросов
        for row in f:  # Цикл для построчного чтения файла и выборки необходимых данных
            remote_address = row.split(' ', 1)[0]  # Сохранение в переменную адреса с которого получен запрос
            temp_request_list = (row.split('"', 2)[1]).split(' ', 2)  # Получение типа и ресурса запроса
            request_type = temp_request_list[0]  # Сохранение типа запроса в переменную
            requested_resource = temp_request_list[1]  # Сохранение ресурса запроса в переменную
            log = (remote_address, request_type, requested_resource)  # Составление кортежа запроса
            request_list.append(log)  # Добавление кортежей запросов в список
        return request_list


if __name__ == '__main__':
    print(request_logs())
