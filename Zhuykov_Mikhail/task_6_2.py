import task_6_1


def spam_request(req_list):
    request_max = dict()
    for el in req_list:
        if el[0] not in request_max:
            request_max[el[0]] = 1
        else:
            request_max[el[0]] = request_max[el[0]] + 1
    max_spam = 0
    max_spam_temp = dict()
    for key, val in request_max.items():
        if val == max_spam:
            max_spam_temp[key] = val
        elif val > max_spam:
            max_spam = val
            max_spam_temp.clear()
            max_spam_temp[key] = val
        else:
            continue
    return (f'Самое большое количество запросов - {v} шт., c IP адреса: {k}' for k, v in max_spam_temp.items())


print(*spam_request(task_6_1.request_logs()))
