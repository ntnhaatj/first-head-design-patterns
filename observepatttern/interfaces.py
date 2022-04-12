from abc import ABC, abstractmethod
from typing import Any


class IDisplay(ABC):
    @classmethod
    @abstractmethod
    def display(cls, *args, **kwargs):
        """ to display """
        pass


class Observer(ABC):
    """ Observer abstract class
    Inherit and implement methods for integrating with Observable
    """
    def __init__(self, observable: "Observable"):
        self.observable = observable
        self.observable.register_observer(self)

    @abstractmethod
    def update(self, data: Any):
        """ to update any data to object state """
        pass


class Observable(ABC):
    def __init__(self):
        self.observers: tuple[Observer] = tuple()

    def register_observer(self, o: Observer):
        """ register new observer """
        self.observers += (o, )

    def remove_observer(self, o: Observer):
        """ remove registered observer """
        self.observers = filter(lambda x: id(o) != id(x), self.observers)

    def notify_all_observers(self):
        """ notify all registered observers """
        data = self.get_data_to_notify()
        for o in self.observers:
            o.update(data)

    @abstractmethod
    def get_data_to_notify(self) -> Any:
        pass
