class Worker:

    def __init__(self, name, surname, position, income):  # Инициализатор класса Worker.
        self.name = name  # Имя сотрудника.
        self.surname = surname  # Фамилия сотрудника.
        self.position = position  # Занимаемая должность.
        self._income = income  # Доход.


class Position(Worker):  # Дочерний класс от класса Worker.
    def __init__(self, name, surname, position, income):  # Инициализатор класса Position.
        super().__init__(name, surname, position, income)  # Параметры наследуемые от родителя.

    def get_full_name(self):
        """Получение полного имени сотрудника"""
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        """Определение дохода с учетом премии"""
        return sum(val for val in self._income.values())


# Экземпляр класса Position - director
post = 'Директор'
salary = {'wage': 150000, 'bonus': 123000}
director = Position('Иван', 'Иванов', post, salary)
print(vars(director))
print(f'{director.position} {director.get_full_name()} '
      f'получил доход с учетом премии {director.get_total_income()} руб.')

# Экземпляр класса Position - engineer
post = 'Инженер'
salary = {'wage': 45000, 'bonus': 23700}
engineer = Position('Петр', 'Петров', post, salary)
print(vars(engineer))
print(f'{engineer.position} {engineer.get_full_name()} '
      f'получил доход с учетом премии {engineer.get_total_income()} руб.')

# Экземпляр класса Position - handyman
post = 'Разнорабочий'
salary = {'wage': 20000, 'bonus': 14500}
handyman = Position('Семен', 'Семенов', post, salary)
print(vars(handyman))
print(f'{handyman.position} {handyman.get_full_name()} '
      f'получил доход с учетом премии {handyman.get_total_income()} руб.')
