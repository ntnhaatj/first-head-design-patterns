from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self):
        self._step_in_order = tuple()

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_want_condiments_hook():
            self.add_condiments()

    def boil_water(self):
        self._step_in_order += ("boiled", )

    @abstractmethod
    def brew(self):
        pass

    def pour_in_cup(self):
        self._step_in_order += ("poured", )

    @abstractmethod
    def add_condiments(self):
        pass

    def customer_want_condiments_hook(self) -> bool:
        return True
    
    def get_recipe_steps(self):
        return self._step_in_order


class Tea(Beverage):
    def brew(self):
        self._step_in_order += ("brewed tea",)

    def add_condiments(self):
        self._step_in_order += ("no condiment",)


class Coffee(Beverage):
    def brew(self):
        self._step_in_order += ("cold brewed",)

    def add_condiments(self):
        self._step_in_order += ("added sugar",)


class TeaWithHook(Beverage):
    def brew(self):
        self._step_in_order += ("brewed tea",)

    def add_condiments(self):
        self._step_in_order += ("added sugar",)

    def customer_want_condiments_hook(self) -> bool:
        add_sugar = input("do you want to add sugar? (input y for yes)")
        if add_sugar == 'y':
            return True
        return False
