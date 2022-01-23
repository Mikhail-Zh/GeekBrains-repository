class Stationery:  # Родительский класс
    title = 'базовый инструмент'

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):  # Дочерний класс
    def __init__(self, title):  # Инициализатор атрибутов экземпляра
        self.title = title

    def draw(self):  # Переопределение метода родительского класса
        print(f'Подписываем ручкой')


class Pencil(Stationery):  # Дочерний класс
    def __init__(self, title):  # Инициализатор атрибутов экземпляра
        self.title = title

    def draw(self):  # Переопределение метода родительского класса
        print(f'Делаем наброски карандашом')


class Handle(Stationery):  # Дочерний класс
    def __init__(self, title):  # Инициализатор атрибутов экземпляра
        self.title = title

    def draw(self):  # Переопределение метода родительского класса
        print(f'Раскрашиваем маркером')


stationery_instance = Stationery()  # Создание экземпляра класса Stationery
pen_instance = Pen('ручка')  # Создание экземпляра класса Pen
pencil_instance = Pencil('карандаш')  # Создание экземпляра класса Pencil
handle_instance = Handle('маркер')  # Создание экземпляра класса Handle

stationery_instance.draw()  # Вызов метода draw
print(f'Инструмент - {stationery_instance.title}\n'
      f'_________________________')

pen_instance.draw()  # Вызов метода draw экземпляра класса Pen
print(f'Инструмент - {pen_instance.title}\n'
      f'_________________________')

pencil_instance.draw()  # Вызов метода draw экземпляра класса Pencil
print(f'Инструмент - {pencil_instance.title}\n'
      f'_________________________')

handle_instance.draw()  # Вызов метода draw экземпляра класса Handle
print(f'Инструмент - {handle_instance.title}\n'
      f'_________________________')
