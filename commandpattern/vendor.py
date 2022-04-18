"""
Home Automation Classes provided by Vendors
"""
from abc import ABC


class VendorBase(ABC):
    def __init__(self, name):
        self.name = name


class Light(VendorBase):
    def on(self):
        msg = f"light {self.name} on"
        return msg

    def off(self):
        msg = f"light {self.name} off"
        return msg


class Door(VendorBase):
    def open(self):
        msg = f"door {self.name} open"
        return msg

    def close(self):
        msg = f"door {self.name} close"
        return msg


class Fan(VendorBase):
    def high(self):
        msg = f"fan {self.name} high"
        return msg

    def medium(self):
        msg = f"fan {self.name} medium"
        return msg

    def low(self):
        msg = f"fan {self.name} low"
        return msg

    def off(self):
        msg = f"fan {self.name} off"
        return msg
