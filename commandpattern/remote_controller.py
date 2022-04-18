from typing import Dict
from dataclasses import dataclass

from .command import Command


@dataclass
class RemoteControllerButtons:
    POS_11 = 'row_1_col_1'
    POS_12 = 'row_1_col_2'
    POS_21 = 'row_2_col_1'
    POS_22 = 'row_2_col_2'


class RemoteController:
    def __init__(self):
        self.buttons: Dict[RemoteControllerButtons, Command] = dict()

    def bind_button_to_command(self, key: RemoteControllerButtons, command: Command):
        self.buttons[key] = command

    def on_button_pressed(self, key: RemoteControllerButtons):
        return self.buttons[key].execute()
