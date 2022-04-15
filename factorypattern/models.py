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
