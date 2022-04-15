import unittest

from factorypattern.models import Fruit, Apple, Orange
from factorypattern import simple_factory, factory_method


class FactoryPatternsTestCase(unittest.TestCase):
    def test_instantiate_fruit_by_simple_factory(self):
        self.assertEqual(
            Orange('orange', 1.0),
            simple_factory.FruitFactory.harvest_orange('orange', 1.0),
        )

        self.assertEqual(
            Apple('red', 1.0),
            simple_factory.FruitFactory.harvest_apple('red', 1.0),
        )

    def test_process_fruit_by_subclasses(self):
        self.assertEqual(
            Apple('red', 1.0, state='peeled'),
            factory_method.AppleExporter.process_fruit('red', 1.0),
        )


if __name__ == '__main__':
    unittest.main()
