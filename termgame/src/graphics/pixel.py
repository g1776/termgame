"""
Description: Define Pixel and RGBColor classes
Author: Gregory Glatzer
Date: 10/20/2022
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from colr import color


class RGBColor:
    def __init__(self, r: int = 0, g: int = 0, b: int = 0):
        self.set(r, "r")
        self.set(g, "g")
        self.set(b, "b")

    def set(self, value: int, channel: str):
        """Set the color for a specific rgb channel. Must be an int between 0-255, inclusive"""

        # check values
        if not (0 <= value <= 255):
            raise ValueError(
                f"Invalid value: {value}. Value must be between 0-255, inclusive"
            )
        if channel not in ["r", "g", "b"]:
            raise ValueError("Channel must be r, g, or b")

        # set value
        self.__setattr__(channel, value)

        return self

    def set_tuple(self, values: Tuple[int, int, int]):
        """Set the color with a full tuple of 3 values between 0-255, inclusive"""
        self.set(values[0], "r")
        self.set(values[1], "g")
        self.set(values[2], "b")
        return self

    def __repr__(self):

        return (self.r, self.g, self.b).__str__()

    def __eq__(self, o: RGBColor):
        return (self.r == o.r) and (self.g == o.g) and (self.b == o.b)

    __str__ = __repr__


@dataclass
class RGBPixel:
    """
    An RGB pixel that can keep track of its color.
    """

    color: RGBColor = RGBColor()
    symbol: str = "\u2001\u2001"
    transparent: bool = False

    def display(self) -> None:
        print(
            color(
                self.symbol,
                fore=(255, 0, 0),
                back=(self.color.r, self.color.g, self.color.b),
            )
        )

    def get(self) -> str:
        return self.__str__()

    def __eq__(self, o: RGBPixel):
        return self.color == o.color

    def __str__(self):
        return color(
            self.symbol,
            fore=(255, 0, 0),
            back=(self.color.r, self.color.g, self.color.b),
        )

    __repr__ = __str__


if __name__ == "__main__":
    p = RGBPixel(color=RGBColor((255, 0, 0)))
    print(p)
