from .interfaces import Beverage


class DarkRoast(Beverage):
    _description = "dark roast"

    def cost(self):
        return 1.0


class Milk(Beverage):
    _description = "milk"

    def cost(self):
        return 2.9
