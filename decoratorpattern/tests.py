import unittest

from decoratorpattern.beverage import DarkRoast, Milk
from decoratorpattern.condiments import Whip, Mocha


class DecoratorPatternTestCase(unittest.TestCase):
    def test_beverage_condiment_decorators(self):
        beverage = DarkRoast()
        mixed_beverage = Whip(Mocha(Mocha(beverage)))
        self.assertEqual(mixed_beverage.get_description(), "dark roast, mocha, mocha, whip")

    def test_beverage_with_condiment_should_add_up_the_cost(self):
        beverage = DarkRoast()
        mixed_beverage = Whip(Mocha(Mocha(beverage)))
        self.assertEqual(mixed_beverage.cost(), 1.8)



if __name__ == '__main__':
    unittest.main()
