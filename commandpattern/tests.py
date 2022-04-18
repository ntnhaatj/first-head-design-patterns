import unittest
from .remote_controller import RemoteController, RemoteControllerButtons as Buttons
from . import command
from . import vendor


class CommandPatternTestCase(unittest.TestCase):
    def test_executing_command_from_remote_controller(self):
        remote = RemoteController()
        light = vendor.Light('living room')

        light_on = command.LightOnCommand(light)
        light_off = command.LightOffCommand(light)

        remote.bind_button_to_command(Buttons.POS_11, light_on)
        remote.bind_button_to_command(Buttons.POS_12, light_off)

        self.assertEqual(remote.on_button_pressed(Buttons.POS_11), "light living room on")
        self.assertEqual(remote.on_button_pressed(Buttons.POS_12), "light living room off")


if __name__ == '__main__':
    unittest.main()
