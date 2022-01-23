class Car:  # Родительский класс
    def __init__(self, speed, color, name, is_police=False):  # Инициализатор
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        """Начало движение транспорта"""
        print(f'Машина {self.name}, цвет {self.color}, цвета поехала')

    def stop(self):
        """Транспорт остановился"""
        print(f'Машина {self.name}, цвет {self.color}, остановилась')

    def turn(self, direction):
        """Транспорт остановился"""
        print(f'Машина {self.name}, цвет {self.color}, повернула {direction}')

    def show_speed(self):
        """Показывает скорость транспорта"""
        print(f'Машина {self.name}, цвет {self.color}, едет со скоростью {self.speed} км/ч')


class TownCar(Car):  # Дочерний класс
    limit_speed = 60

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        """
        Переопределение метода родительского класса. Показывает скорость транспорта, если скорость больше
        разрешенной выводит сообщение о превышении скорости
        """
        if self.speed > self.limit_speed:
            print(f'Машина {self.name}, цвет {self.color}, превысила скорость на {self.speed - self.limit_speed} км/ч')
        if self.speed <= self.limit_speed:
            print(f'Машина {self.name}, цвет {self.color}, едет со скоростью {self.speed} км/ч')


class SportCar(Car):  # Дочерний класс
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):  # Дочерний класс
    limit_speed = 40

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        """Переопределение метода родительского класса. Показывает скорость транспорта, если скорость больше
        разрешенной выводит сообщение о превышении скорости"""
        if self.speed > self.limit_speed:
            print(f'Машина {self.name}, цвет {self.color}, превысила скорость на {self.speed - self.limit_speed} км/ч')
        if self.speed <= self.limit_speed:
            print(f'Машина {self.name}, цвет {self.color}, едет со скоростью {self.speed} км/ч')


class PoliceCar(Car):  # Дочерний класс
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(50, 'Green', 'Audi A1', False)  # Создание экземпляра класса TownCar
sport_car = SportCar(200, 'Black', 'Bugatti Veyron', False)  # Создание экземпляра класса SportCar
work_car = WorkCar(30, 'Red', 'КамАЗ 6180', False)  # Создание экземпляра класса WorkCar
police_car = PoliceCar(130, 'Blue', 'Police Vehicle', True)  # Создание экземпляра класса PoliceCar

print(vars(town_car))  # Печать атрибутов экземпляра town_car
print(vars(sport_car))  # Печать атрибутов экземпляра sport_car
print(vars(work_car))  # Печать атрибутов экземпляра work_car
print(vars(police_car))  # Печать атрибутов экземпляра police_car

town_car.show_speed()  # Вызов метода show_speed
sport_car.go()  # Вызов метода go
work_car.stop()  # Вызов метода stop
police_car.show_speed()  # Вызов метода show_speed

town_car.speed = 85  # Изменение атрибута speed у экземпляра town_car
print(vars(town_car))  # Печать атрибутов экземпляра town_car
town_car.show_speed()  # Вызов метода show_speed
