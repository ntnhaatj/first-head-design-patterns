from .interfaces import CondimentDecorator, Beverage


class Whip(CondimentDecorator):
    _description = "whip"

    def __init__(self, beverage: Beverage):
        super().__init__(beverage)

    def cost(self):
        return 0.2 + self.beverage.cost()

    def get_description(self):
        return ', '.join((self.beverage.get_description(), self._description))


class Mocha(CondimentDecorator):
    _description = "mocha"

    def __init__(self, beverage: Beverage):
        super().__init__(beverage)

    def cost(self):
        return 0.3 + self.beverage.cost()

    def get_description(self):
        return ', '.join((self.beverage.get_description(), self._description))
