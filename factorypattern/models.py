from dataclasses import dataclass, field


@dataclass
class Fruit:
    color: str
    weight: float
    name: str = field(default='Unknown Fruit', init=False)
    state: str = field(default=None, init=True)


@dataclass
class Apple(Fruit):
    name = 'Apple'


@dataclass
class Orange(Fruit):
    name = 'Orange'


@dataclass
class OrganicMixin:
    is_organic = True


@dataclass
class NonOrganicMixin:
    is_organic = False


@dataclass
class OrganicFruit(Fruit, OrganicMixin):
    pass


@dataclass
class NonOrganicFruit(Fruit, NonOrganicMixin):
    pass


@dataclass
class OrganicApple(OrganicFruit):
    name = 'Apple'


@dataclass
class OrganicOrange(OrganicFruit):
    name = 'Orange'


@dataclass
class NonOrganicApple(NonOrganicFruit):
    name = 'Apple'


@dataclass
class NonOrganicOrange(NonOrganicFruit):
    name = 'Orange'
