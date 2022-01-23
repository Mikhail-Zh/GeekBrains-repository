from time import sleep


class TrafficLight:
    __color = None  # В переменной хранится текущее значение цвета

    def running(self, color_light):
        if color_light == 'красный' and \
                (self.__color == 'зеленый' or self.__color is None):  # Условие для включения красного
            print(f'\033[31m {"Включился красный"}')
            self.__color = 'красный'
            sleep(7)
            print(f'\033[0m {"Красный отключен"}')
        elif color_light == 'желтый' and self.__color == 'красный':  # Условие для включения желтого
            print(f'\033[33m {"Включился жёлтый"}')
            self.__color = 'желтый'
            sleep(2)
            print(f'\033[0m {"Желтый отключен"}')
        elif color_light == 'зеленый' and self.__color == 'желтый':  # Условие для включения зеленого
            print(f'\033[32m {"Включился зелёный"}')
            self.__color = 'зеленый'
            sleep(5)
            print(f'\033[0m {"Зеленый отключен"}')
        else:
            print('Нарушен порядок следования цвета')


first_traffic_light = TrafficLight()
first_traffic_light.running(color_light='красный')
first_traffic_light.running(color_light='желтый')
first_traffic_light.running(color_light='зеленый')
first_traffic_light.running(color_light='красный')
first_traffic_light.running(color_light='зеленый')
first_traffic_light.running(color_light='зеленый')

