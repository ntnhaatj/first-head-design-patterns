""" Simple Factory Example """
from .models import Apple, Orange


class FruitFactory:
    @staticmethod
    def harvest_apple(color: str, weight: float):
        return Apple(color=color, weight=weight)

    @staticmethod
    def harvest_orange(color: str, weight: float):
        return Orange(color=color, weight=weight)
