import sys


class Warehouse:  # Класс Склад
    section_printer = {}  # Словарь для хранения информации, в отделе хранения принтеров.
    section_scanner = {}  # Словарь для хранения информации, в отделе хранения сканеров.
    section_xerox = {}  # Словарь для хранения информации, в отделе хранения ксероксов.
    last_num_storage_printer = 1000  # Номер места хранения оборудования в отделе принтеров. Начало с 1000.
    last_num_storage_scanner = 1000  # Номер места хранения оборудования в отделе сканеров. Начало с 1000.
    last_num_storage_xerox = 1000  # Номер места хранения оборудования в отделе ксероксов. Начало с 1000.

    def __init__(self, type_equipment, quantity):  # Инициализатор
        self.type_equipment = type_equipment  # Получение товара.
        try:
            self.quantity = int(quantity)  # Количество товара.
        except ValueError:  # Если введены символы, а не число.
            print(f'Значение количество оборудования должно быть числом')
            sys.exit()  # Выход из программы если поймаем ошибку

    def receiving_transfer(self):
        """Метод для приемки и передачи оргтехники в отделы хранения склада"""
        if self.type_equipment.type_technic == 'printer':  # Условие для отправки в отдел принтеров.
            return Warehouse.storage_printer(self.type_equipment, self.quantity)  # Отправка в отдел принтеров.
        elif self.type_equipment.type_technic == 'scanner':  # Условие для отправки в отдел сканеров.
            return Warehouse.storage_scanner(self.type_equipment, self.quantity)  # Отправка в отдел сканеров.
        elif self.type_equipment.type_technic == 'xerox':  # Условие для отправки в отдел ксероксов.
            return Warehouse.storage_xerox(self.type_equipment, self.quantity)  # Отправка в отдел ксероксов.
        else:  # Если ничего не отправилось, значит в параметрах оргтехники неправильно указана группа.
            return f'У оборудования не верно указана группа оргтехники'

    def storage_printer(self, item):
        """Метод для учета в отделе хранения принтеров"""
        for el in range(item):  # Цикл для присвоения каждой единице товара номера места хранения. Если несколько штук.
            Warehouse.last_num_storage_printer += 1  # Создание номера места хранения в отделе.
            Warehouse.section_printer[Warehouse.last_num_storage_printer] = vars(self)  # Запись данных в словарь.
        return Warehouse.section_printer  # Возврат списка оборудования в отделе принтеров.

    def storage_scanner(self, item):
        """Метод для учета в отделе хранения сканеров"""
        for el in range(item):  # Цикл для присвоения каждой единице товара номера места хранения. Если несколько штук.
            Warehouse.last_num_storage_scanner += 1  # Создание номера места хранения в отделе.
            Warehouse.section_scanner[Warehouse.last_num_storage_scanner] = vars(self)  # Запись данных в словарь.
        return Warehouse.section_scanner  # Возврат списка оборудования в отделе сканеров.

    def storage_xerox(self, item):
        """Метод для учета в отделе хранения xerox"""
        for el in range(item):  # Цикл для присвоения каждой единице товара номера места хранения. Если несколько штук.
            Warehouse.last_num_storage_xerox += 1  # Создание номера места хранения в отделе.
            Warehouse.section_xerox[Warehouse.last_num_storage_xerox] = vars(self)  # Запись данных в словарь.
        return Warehouse.section_xerox  # Возврат списка оборудования в отделе ксероксов.

    def shipping_warehouse(self, storage_location):
        """Метод для отгрузки оргтехники со склада"""
        if self.type_equipment.type_technic == 'printer':  # Условие для удаления оборудования, номера места хранения.
            del Warehouse.section_printer[storage_location]  # Удаление из отдела принтеров.
            return Warehouse.section_printer  # Для проверки: Возвращает словарь оборудования отдела принтеров.
        elif self.type_equipment.type_technic == 'scanner':  # Условие для удаления оборудования, номера места хранения.
            del Warehouse.section_scanner[storage_location]  # Удаление из отдела сканеров.
            return Warehouse.section_scanner  # Для проверки: Возвращает словарь оборудования отдела сканеров.
        elif self.type_equipment.type_technic == 'xerox':  # Условие для удаления оборудования, номера места хранения.
            del Warehouse.section_xerox[storage_location]  # Удаление из отдела сканеров.
            return Warehouse.section_xerox  # Условие для удаления оборудования, номера места ксероксов.
        else:
            return f'Оборудование не удалено. У оборудования не верно указана группа оргтехники'


class OfficeTechnic:
    def __init__(self, type_technic, brand, model, for_home):
        self.type_technic = type_technic  # Тип оборудования 'printer', 'scanner', 'xerox'.
        self.brand = brand  # Марка.
        self.model = model  # Модель
        self.for_home = for_home  # Для дома или для офиса


class Printer(OfficeTechnic):
    def __init__(self, type_technic, brand, model, for_home, printer_type, print_speed):
        self.printer_type = printer_type  # Тип принтера: струйный, лазерный, матричный
        self.print_speed = print_speed  # Скорость печати.
        super().__init__(type_technic, brand, model, for_home)


class Scanner(OfficeTechnic):
    def __init__(self, type_technic, brand, model, for_home, scanner_type, scan_speed):
        self.scan_type = scanner_type  # Тип сканера: цветной, ч/б.
        self.print_speed = scan_speed  # Скорость сканирования.
        super().__init__(type_technic, brand, model, for_home)


class Xerox(OfficeTechnic):
    def __init__(self, type_technic, brand, model, for_home, scanner_type, printer_type, copy_speed):
        self.scanner_type = scanner_type  # Тип сканера: цветной, ч/б.
        self.printer_type = printer_type  # Скорость печати.
        self.print_speed = copy_speed  # Скорость копирования.
        super().__init__(type_technic, brand, model, for_home)


printer_1 = Printer('printer', 'HP', 777, True, 'laser', 100)  # Создание экземпляра класса Printer
scanner_1 = Scanner('scanner', 'SS', 888, False, 'color', 300)  # Создание экземпляра класса Scanner
xerox_1 = Xerox('xerox', 'MM', 999, True, 'color', 'laser', 200)  # Создание экземпляра класса Xerox
xerox_2 = Xerox('xerox', 'NN', 101010, False, 'no color', 'laser', 250)  # Создание экземпляра класса Xerox

printer_receipt = Warehouse(printer_1, 25)  # Отправка принтеров на склад
print(printer_receipt.receiving_transfer())
print('-'*25)
scanner_receipt = Warehouse(scanner_1, 15)  # Отправка сканеров на склад
print(scanner_receipt.receiving_transfer())
print('-'*25)
xerox_receipt = Warehouse(xerox_1, 10)  # Отправка ксероксов на склад
print(xerox_receipt.receiving_transfer())
print('-'*25)
xerox_receipt = Warehouse(xerox_2, 3)  # Отправка ксероксов на склад
print(xerox_receipt.receiving_transfer())
print('-'*25)
print(xerox_receipt.shipping_warehouse(1002))  # Удаление ксерокса со склада с места хранения 1002
