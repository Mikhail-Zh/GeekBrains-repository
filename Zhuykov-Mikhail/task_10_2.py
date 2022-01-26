from abc import ABC, abstractmethod


class Clothes(ABC):  # Абстрактный класс.
    used_fabric = 0  # Переменная для хранения общего расхода ткани.

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):  # Дочерний класс.

    def __init__(self, v):  # Инициализатор.
        self.v = v

    @property  # Декоратор
    def fabric_consumption(self):
        """Функция подсчета необходимого количества ткани на пальто"""
        fabric_cons = round(self.v / 6.5 + 0.5, 2)  # Расчет необходимого количества ткани.
        Clothes.used_fabric += fabric_cons  # Прибавление необходимой ткани к общему расходу.
        return fabric_cons


class Suit(Clothes):  # Дочерний класс.

    def __init__(self, h):  # Инициализатор.
        self.h = h

    @property  # Декоратор
    def fabric_consumption(self):
        """Функция подсчета необходимого количества ткани на костюм"""
        fabric_cons = round(2 * self.h + 0.3, 2)  # Расчет необходимого количества ткани.
        Clothes.used_fabric += fabric_cons  # Прибавление необходимой ткани к общему расходу.
        return fabric_cons


Coat_1 = Coat(46)  # Создание экземпляра класса.
Coat_2 = Coat(48)  # Создание экземпляра класса.
Coat_3 = Coat(50)  # Создание экземпляра класса.
Suit_1 = Suit(1.65)  # Создание экземпляра класса.
Suit_2 = Suit(1.8)  # Создание экземпляра класса.
Suit_3 = Suit(1.95)  # Создание экземпляра класса.

print(Coat_1.fabric_consumption)  # Получение данных о необходимом количестве ткани.
print(Coat_2.fabric_consumption)  # Получение данных о необходимом количестве ткани.
print(Coat_3.fabric_consumption)  # Получение данных о необходимом количестве ткани.

print(Suit_1.fabric_consumption)  # Получение данных о необходимом количестве ткани.
print(Suit_2.fabric_consumption)  # Получение данных о необходимом количестве ткани.
print(Suit_3.fabric_consumption)  # Получение данных о необходимом количестве ткани.

print(Clothes.used_fabric)  # Получение данных о полном расходе ткани.
