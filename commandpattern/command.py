from typing import Any

from abc import ABC, abstractmethod
from . import vendor


class Command(ABC):
    """ define `command` interface
    concrete command will implement below methods """
    @abstractmethod
    def execute(self) -> Any:
        return None


class LightOnCommand(Command):
    def __init__(self, light: vendor.Light):
        self.light = light

    def execute(self):
        return self.light.on()


class LightOffCommand(Command):
    def __init__(self, light: vendor.Light):
        self.light = light

    def execute(self):
        return self.light.off()


class FanHighCommand(Command):
    def __init__(self, fan: vendor.Fan):
        self.fan = fan

    def execute(self):
        return self.fan.high()


class FanLowCommand(Command):
    def __init__(self, fan: vendor.Fan):
        self.fan = fan

    def execute(self):
        return self.fan.high()


class FanOffCommand(Command):
    def __init__(self, fan: vendor.Fan):
        self.fan = fan

    def execute(self):
        return self.fan.high()
