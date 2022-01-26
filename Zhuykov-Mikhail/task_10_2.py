from abc import ABC, abstractmethod


class Clothes(ABC):
    pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    @property
    def fabric_consumption(self):
        pass


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @abstractmethod
    @property
    def fabric_consumption(self):
        pass