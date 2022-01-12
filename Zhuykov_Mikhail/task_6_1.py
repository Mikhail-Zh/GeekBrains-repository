def request_logs():
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
        request_list = []
        for row in f:
            remote_addr = row.split(' ', 1)[0]
            temp_request_list = (row.split('"', 2)[1]).split(' ', 2)
            request_type = temp_request_list[0]
            requested_resource = temp_request_list[1]
            log = (remote_addr, request_type, requested_resource)
            request_list.append(log)
        return request_list


if __name__ == '__main__':
    print(request_logs())
