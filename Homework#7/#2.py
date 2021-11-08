
from abc import ABC, abstractmethod

class Material(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def get_consumption(self):
        pass


class Coat(Material):
    def __init__(self, param):
        super().__init__(param)
        print(f' Это новое пальто с размером {self.param}')

    @property
    def get_consumption(self):
        return (self.param / 6.5 + 0.5)


class Suit(Material):
    def __init__(self, param):
        super().__init__(param)
        print(f' Это новый костюм с размером {self.param}')

    @property
    def get_consumption(self):
        return (self.param * 2 + 0.3)


my_coat = Coat(46)
print(f' Расход ткани для пальто: {my_coat.get_consumption}')
my_suit = Suit(1.75)
print(f'Расход ткани для костюма: {my_suit.get_consumption}')
print(f'Суммарный расход ткани: {my_coat.get_consumption + my_suit.get_consumption}')

