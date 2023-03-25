"""
Description: This file defines two classes for working with RGB colors: RGBColor and RGBPixel. 
    RGBColor is a simple class for representing an RGB color with values between 0-255 for the red, green, and blue channels. 
    RGBPixel extends RGBColor to include a symbol and transparency value for displaying pixels in a terminal. 
Author: Gregory Glatzer
Date: 3/25/2023
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from colr import color  # type: ignore


class RGBColor:
    """
    Represents an RGB color. It stores values for red, green, and blue channels, each with a range of 0 to 255.
    """

    def __init__(self, r: int = 0, g: int = 0, b: int = 0) -> None:
        """
        Initialize an RGBColor object with the given red, green, and blue channel values.

        :param r: The red channel value. Defaults to 0.
        :type r: int
        :param g: The green channel value. Defaults to 0.
        :type g: int
        :param b: The blue channel value. Defaults to 0.
        :type b: int
        """

        self.r = 0
        self.g = 0
        self.b = 0
        self.set(r, "r")
        self.set(g, "g")
        self.set(b, "b")

    def set(self, value: int, channel: str) -> RGBColor:
        """Set the color value for a specific RGB channel.

        :param value: An integer value between 0 and 255, inclusive, representing the color value to set.
        :type value: int
        :param channel: The channel for which to set the color value. Must be one of "r", "g", or "b".
        :type channel: str
        :return: The updated RGBColor object.
        :rtype: RGBColor
        :raises ValueError: If the value is not between 0 and 255, inclusive, or if the channel is not one of "r", "g", or "b".
        """

        # Check the validity of the input values
        if not 0 <= value <= 255:
            raise ValueError(f"Invalid value: {value}. Value must be between 0-255, inclusive")
        if channel not in ["r", "g", "b"]:
            raise ValueError("Channel must be r, g, or b")

        # Set the color value
        self.__setattr__(channel, value)

        return self

    def set_tuple(self, values: Tuple[int, int, int]) -> RGBColor:
        """
        Sets the color for the RGB channels using a tuple of 3 integer values between 0-255, inclusive.

        :param values: A tuple of 3 integers representing the RGB values of the color.
        :type values: Tuple[int, int, int]
        :return: Returns the updated RGBColor object after setting the RGB values.
        :rtype: RGBColor
        :raises ValueError: If the input values are not integers between 0-255, inclusive.
        """
        self.set(values[0], "r")
        self.set(values[1], "g")
        self.set(values[2], "b")
        return self

    def __repr__(self):
        """
        Return a string representation of the RGBColor object.

        :return: A string representation of the RGBColor object.
        :rtype: str
        """

        return (self.r, self.g, self.b).__str__()

    def __eq__(self, other: object) -> bool:
        """
        Check if this RGBColor object is equal to another object.

        :param other: The object to compare to.
        :type other: object
        :raises NotImplementedError: If the other object is not of type RGBColor.
        :return: True if the objects are equal, False otherwise.
        :rtype: bool
        """

        if not isinstance(other, RGBColor):
            raise NotImplementedError(f"Cannot compare RGBColor to {type(other)}")

        return (self.r == other.r) and (self.g == other.g) and (self.b == other.b)

    __str__ = __repr__


@dataclass
class RGBPixel:
    """
    A class representing an RGB pixel that can keep track of its color.

    Attributes
    ----------
    color : RGBColor
        The color of the pixel in RGB format.
    symbol : str, optional
        The symbol that represents the pixel (default "\u2001\u2001").
    transparent : bool, optional
        Whether the pixel is transparent (default False).

    Methods
    -------
    display() -> None:
        Prints the pixel to the console with its current color.
    get() -> str:
        Returns a string representation of the pixel with its current color.
    __eq__(self, other: object) -> bool:
        Compares the pixel with another object for equality.

    Notes
    -----
    A pixel's color can be set by creating an RGBColor object and passing it to the constructor.
    """

    color: RGBColor = RGBColor()
    symbol: str = "\u2001\u2001"
    transparent: bool = False

    def display(self) -> None:
        """
        Prints the pixel to the console with its current color.
        """
        print(
            color(
                self.symbol,
                fore=(255, 0, 0),
                back=(self.color.r, self.color.g, self.color.b),
            )
        )

    def get(self) -> str:
        """
        Returns a string representation of the pixel with its current color.
        """
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        """
        Compares the pixel with another object for equality.

        Parameters
        ----------
        other : object
            The object to compare with.

        Returns
        -------
        bool
            True if the objects are equal, False otherwise.
        """
        if not isinstance(other, RGBPixel):
            return NotImplementedError(f"Cannot compare RGBPixel to {type(other)}")
        return self.color == other.color

    def __str__(self) -> str:
        """
        Returns a string representation of the pixel with its current color.
        """
        return color(
            self.symbol,
            fore=(255, 0, 0),
            back=(self.color.r, self.color.g, self.color.b),
        )

    __repr__ = __str__


if __name__ == "__main__":
    p = RGBPixel(color=RGBColor(*(255, 0, 0)))
    print(p)
