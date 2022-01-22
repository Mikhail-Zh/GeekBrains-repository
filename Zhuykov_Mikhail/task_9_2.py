class Road:

    def __init__(self, mass, height):  # Инициализатор класса Road.
        self._length = 20  # Атрибут экземпляра.
        self._width = 5000  # Атрибут экземпляра.
        self.mass = mass  # Атрибут экземпляра.
        self.height = height  # Атрибут экземпляра.

    def asphalt_mass(self):
        """
        Метод класса Road. Определяет сколько необходимо тонн асфальта при строительстве дороги.
        """
        print(f'Потребуется {(self._length * self._width * self.mass * self.height)/1000} тонн асфальта')


road_to_perm = Road(mass=25, height=5)  # Создание экземпляра класса.
print(vars(road_to_perm))  # Проверил, что атрибуты передались при создании экземпляра класса.
road_to_perm.asphalt_mass()  # Проверка работы метода.
