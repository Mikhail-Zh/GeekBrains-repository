import re


def email_parse(email_address):
    """
    Функция принимает email-адрес и проверяет его на правильность. В случае не правильного ввода адреса возвращает
    ошибку - raise ValueError(msg) и сообщение ValueError: wrong email: 'email-адрес'. Если адрес введен верно -
    возвращает имя пользователя 'username' и домен 'domain'.
    """
    try:
        pattern = re.compile(
            r'(?P<username>^[а-яА-ЯёЁa-zA-Z0-9][\w.-]*[а-яА-ЯёЁa-zA-Z0-9])@'
            r'(?P<domain>[а-яА-ЯёЁa-zA-Z0-9](?:[а-яА-ЯёЁa-zA-Z0-9.-]+)*[а-яА-ЯёЁa-zA-Z0-9]\.'
            r'[а-яА-ЯёЁa-zA-Z0-9]+)$')  # Шаблон для проверки email-адреса
        result_iter = pattern.finditer(email_address)
        assert pattern.match(email_address)  # Проверка соответствия email-адреса шаблону
        for word in result_iter:  # Цикл для вывода групп шаблона <username> и <domain>
            return word.groupdict()
    except AssertionError:
        msg = f'wrong email: {email_address}'  # Сообщение если email-адрес не соответствует шаблону
        raise ValueError(msg)


print(email_parse('Mikhail@mail.ru'))
