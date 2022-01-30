from datetime import datetime


class Date:  # Класс Date
    def __init__(self, str_date):  # Инициализатор
        self.str_date = str_date

    @classmethod
    def date_conversion(cls, param):
        """Метод преобразует дату из строки формата dd-mm-YYYY в кортеж чисел"""
        tuple_date = tuple(int(i) for i in (param.split('-')))  # Преобразование строки даты в кортеж чисел
        return tuple_date

    @staticmethod
    def valid_date(obj):
        """Метод определяет правильность полученной даты"""
        try:
            datetime.strptime(obj.str_date, '%d-%m-%Y')  # Преобразование строки в дату.
        except ValueError:  # Если даты нет или не тот формат - ValueError.
            return f'Дата указана не в том формате или такой даты не существует'
        else:
            return Date.date_conversion(obj.str_date)  # Если ошибок не было, данные передаются в методу date_conversion


instance_date_1 = Date('29-02-2000')  # Дата в високосном году (существующая дата).
print(instance_date_1.valid_date(instance_date_1))

instance_date_2 = Date('29-02-2001')  # Не существующая дата. Неверно указано число.
print(instance_date_2.valid_date(instance_date_2))

instance_date_3 = Date('12-11-2022')  # Существующая дата
print(instance_date_3.valid_date(instance_date_3))

instance_date_4 = Date('12-15-2000')  # Не существующая дата. Неверно указан месяц.
print(instance_date_4.valid_date(instance_date_4))

instance_date_5 = Date('12.15.2000')  # Неверно указан формат строки.
print(instance_date_5.valid_date(instance_date_5))
