from abc import ABC, abstractmethod

from .models import Fruit, Orange, Apple


def wash(fruit: Fruit):
    fruit.state = 'washed'
    return fruit


def peel(fruit: Fruit):
    fruit.state = 'peeled'
    return fruit


class FruitExporter(ABC):
    @classmethod
    @abstractmethod
    def harvest_fruit(cls, color, weight) -> Fruit:
        """ this is factory method """
        pass

    @classmethod
    def process_fruit(cls, color, weight):
        fruit = cls.harvest_fruit(color, weight)
        fruit = wash(fruit)
        fruit = peel(fruit)
        return fruit


class OrangeExporter(FruitExporter):
    @classmethod
    def harvest_fruit(cls, color, weight) -> Fruit:
        return Orange(color, weight)


class AppleExporter(FruitExporter):
    @classmethod
    def harvest_fruit(cls, color, weight) -> Fruit:
        return Apple(color, weight)
