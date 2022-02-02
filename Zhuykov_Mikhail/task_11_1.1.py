class Date:
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
            day, month, year = obj.str_date.split('-')  # Выделение из полученной строки числа месяца и года.
            day = int(day)  # Приведение полученного числа к типу int.
            month = int(month)  # Приведение полученного месяца к типу int.
            year = int(year)  # Приведение полученного года к типу int.
        except ValueError:
            return f'Не верный формат даты'

        day_in_months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30,
                         12: 31}  # Словарь с количеством дней в каждом месяце.
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):  # Определение високосного года.
            day_in_months[2] = 29  # Если год високосный в словаре изменить число дней в феврале.
        try:
            if 1 <= day <= day_in_months[month]:  # Проверка, что полученное число находится в диапазоне чисел месяца.
                return Date.date_conversion(obj.str_date)
            else:  # Если число находится не в диапазоне чисел месяца.
                return f'Не верно указан день месяца'
        except KeyError:  # Если в полученной дате числовое значение месяца больше чем 12.
            return f'Не верно указан номер месяца'


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
