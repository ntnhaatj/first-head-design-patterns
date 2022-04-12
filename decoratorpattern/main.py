from decoratorpattern.beverage import DarkRoast, Milk
from decoratorpattern.condiments import Whip, Mocha


if __name__ == "__main__":
    dark_roast = DarkRoast()
    dark_roast = Whip(dark_roast)
    dark_roast = Mocha(dark_roast)

    print(dark_roast.get_description())
