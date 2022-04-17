from abc import ABC, abstractmethod

from .models import Fruit, OrganicFruit, NonOrganicFruit, OrganicApple, OrganicOrange, NonOrganicApple, NonOrganicOrange


class FruitExporter(ABC):
    @classmethod
    @abstractmethod
    def harvest_fruit(cls, color, weight) -> Fruit:
        """ this is factory method """
        pass


class OrganicExporter(FruitExporter):
    @classmethod
    @abstractmethod
    def harvest_fruit(cls, color, weight) -> OrganicFruit:
        pass


class NonOrganicExporter(FruitExporter):
    @classmethod
    @abstractmethod
    def harvest_fruit(cls, color, weight) -> NonOrganicFruit:
        pass


class OrganicAppleExporter(OrganicExporter):
    @classmethod
    def harvest_fruit(cls, color, weight) -> OrganicFruit:
        return OrganicApple(color, weight)


class OrganicOrangeExporter(OrganicExporter):
    @classmethod
    def harvest_fruit(cls, color, weight) -> OrganicFruit:
        return OrganicOrange(color, weight)


class NonOrganicAppleExporter(NonOrganicExporter):
    @classmethod
    def harvest_fruit(cls, color, weight) -> NonOrganicFruit:
        return NonOrganicApple(color, weight)


class NonOrganicOrangeExporter(NonOrganicExporter):
    @classmethod
    def harvest_fruit(cls, color, weight) -> NonOrganicFruit:
        return NonOrganicOrange(color, weight)
