from time import sleep, perf_counter


class TrafficLight:  # В переменной хранится текущее значение цвета
    __color = None

    def running(self, t_work=60):
        """
        Функция включения светофора.
        t_work -
        """
        start = perf_counter()
        while True:  # Цикл для вывода сигналов светофора
            if perf_counter() - start >= t_work:  # Проверка заданного времени работы светофора
                break
            if self.__color == 'зелёный' or self.__color is None:  # Условие для включения красного
                print(f'\033[31m {"Включился красный"}')
                self.__color = 'красный'
                sleep(7)
            elif self.__color == 'красный':  # Условие для включения желтого
                print(f'\033[33m {"Включился жёлтый"}')
                self.__color = 'жёлтый'
                sleep(2)
            elif self.__color == 'жёлтый':  # Условие для включения зеленого
                print(f'\033[32m {"Включился зелёный"}')
                self.__color = 'зелёный'
                sleep(5)
        return f'\033[0m {"Светофор отключен"}'


ret = TrafficLight()
print(ret.running(t_work=17))
