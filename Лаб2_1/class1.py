# TODO Написать 3 класса с документацией и аннотацией типов

import doctest

class Laptop:
    def __init__(self, brand: str, model: str, price: float):
        """
        Create a new Laptop object.

        :param brand: The brand of the laptop
        :param model: The model of the laptop
        :param price: The price of the laptop

        Examples:
        >>> laptop = Laptop("Lenovo", "ThinkPad", 1200.00)
        """
        self.brand = brand
        self.model = model
        self.price = price

    def turn_on(self):
        """
        Turn on the laptop.

        Examples:
        >>> laptop = Laptop("Lenovo", "ThinkPad", 1200.00)
        >>> laptop.turn_on()
        """
        ...

    def turn_off(self):
        """
        Turn off the laptop.

        Examples:
        >>> laptop = Laptop("Lenovo", "ThinkPad", 1200.00)
        >>> laptop.turn_off()
        """
        ...


class Lamp:
    def __init__(self, color: str, power: int, is_on: bool):
        """
        Create a new Lamp object.

        :param color: The color of the lamp
        :param power: The power of the lamp
        :param is_on: Whether the lamp is turned on or off

        Examples:
        >>> lamp = Lamp("White", 60, True)
        """
        self.color = color
        self.power = power
        self.is_on = is_on

    def switch_on(self):
        """
        Switch on the lamp.

        Examples:
        >>> lamp = Lamp("White", 60, False)
        >>> lamp.switch_on()
        """
        ...

    def switch_off(self):
        """
        Switch off the lamp.

        Examples:
        >>> lamp = Lamp("White", 60, True)
        >>> lamp.switch_off()
        """
        ...


class Keyboard:
    def __init__(self, layout: str, language: str, num_keys: int):
        """
        Create a new Keyboard object.

        :param layout: The layout of the keyboard
        :param language: The language of the keyboard
        :param num_keys: The number of keys on the keyboard

        Examples:
        >>> keyboard = Keyboard("QWERTY", "English", 104)
        """
        self.layout = layout
        self.language = language
        self.num_keys = num_keys

    def press_key(self):
        """
        Simulate pressing a key on the keyboard.

        Examples:
        >>> keyboard = Keyboard("QWERTY", "English", 104)
        >>> keyboard.press_key()
        """
        ...

    def clean_key(self):
        """
        Clean a key on the keyboard.

        Examples:
        >>> keyboard = Keyboard("QWERTY", "English", 104)
        >>> keyboard.clean_key()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
