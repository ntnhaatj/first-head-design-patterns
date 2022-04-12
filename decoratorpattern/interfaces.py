""" This component should be closed for modification
"""

from abc import ABC, abstractmethod


class Beverage(ABC):
    _description = "Unknown beverage"

    @abstractmethod
    def cost(self):
        pass

    def get_description(self):
        return self._description


class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        super(CondimentDecorator, self).__init__()
        self.beverage = beverage

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def get_description(self):
        """ force concrete decorators reimplement this method
        inherit should be only aim for making the same type with super class """
        pass
