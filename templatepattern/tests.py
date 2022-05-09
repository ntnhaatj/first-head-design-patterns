import unittest
from unittest.mock import patch, Mock

from templatepattern.beverage import *


class TemplatePatternTestCase(unittest.TestCase):

    def test_all_beverage_recipe_steps_follow_template(self):
        tea = Tea()
        tea.prepare_recipe()
        self.assertEqual(tea.get_recipe_steps(), ("boiled", "brewed tea", "poured", "no condiment"))

        coffee = Coffee()
        coffee.prepare_recipe()
        self.assertEqual(coffee.get_recipe_steps(), ("boiled", "cold brewed", "poured", "added sugar"))

    @patch("builtins.input", lambda *arg: 'y')
    def test_tea_with_hook_when_user_want_condiment(self):
        tea = TeaWithHook()
        tea.prepare_recipe()
        self.assertEqual(tea.get_recipe_steps(), ("boiled", "brewed tea", "poured", "added sugar"))

    @patch("builtins.input", lambda *arg: 'n')
    def test_tea_with_hook_when_user_doesnt_want_condiment(self):
        tea = TeaWithHook()
        tea.prepare_recipe()
        self.assertEqual(tea.get_recipe_steps(), ("boiled", "brewed tea", "poured",))


if __name__ == '__main__':
    unittest.main()
