from datetime import datetime
from decimal import Decimal
from requests import get


def currency_rates(curr_name):
    """
    Функция возвращает курс валюты с сайта 'http://www.cbr.ru/scripts/XML_daily.asp'.
    Если валюта указана неверно возвращает 'None'.
    В качестве аргумента принимает код валюты (например, USD, EUR, GBP, ...).
    """
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')  # Запрос к сайту.
    text = response.text  # Получение контента.
    curr_name = curr_name.upper()  # Приведение регистра аргумента к виду ответа сайта.
    if text.find(curr_name) != -1:  # Проверка наличия валюты на сайте.
        request_date = text.split('Date="')[1]  # Нахождение даты в ответе сайта.
        request_date = request_date.split('"')[0]
        request_date = datetime.strptime(request_date, '%d.%m.%Y').date()  # Получение даты в нужном формате.
        currency = {"Nominal": 0, "Value": 0}  # Определения словаря. Для записи полученных ниже данных с сайта.
        val = text[text.find(curr_name):]  # Получение среза данных от места нахождения искомой валюты.
        for k in currency.keys():  # Цикл для получения значений для ключей словаря 'currency'.
            el = val.split(f'<{k}>')
            el = el[1].split(f'</{k}>')
            currency[k] = el[0].replace(",", ".")  # Замена запятой на точку в курсе валюты.
        curr_value = (Decimal(currency["Value"]) / Decimal(currency["Nominal"]))
        return f'{float(curr_value.quantize(Decimal(".01")))}, {request_date}'  # Возврат курса валюты и даты с сайта.
    else:  # Возврат значения "None" если код валюты указан неверно.
        return "None"


if __name__ == "__main__":
    print(currency_rates("USD"))
    print(currency_rates("Eur"))
    print(currency_rates("VSD"))