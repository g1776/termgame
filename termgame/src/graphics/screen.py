"""
Description: Define the Screen class.
Author: Gregory Glatzer
Date: 10/22/2022
"""

from __future__ import annotations

from typing import Tuple

import numpy as np
from PIL import Image

from .pixel import RGBColor, RGBPixel


class Screen:
    def __init__(self, width: int, height: int):

        self.width = width
        self.height = height
        # define the screen as a cleared screen (all pixels are black)
        self.clear()

    def set_px(self, px: RGBPixel, x: int, y: int) -> Screen:
        """Set pixel at (x,y) on the screen to a new pixel"""
        self.__check_coordinate(x, y)
        self.pixels[y][x] = px
        return self

    def set_px_color(self, color: Tuple[int, int, int], x: int, y: int) -> Screen:
        """Shorthand to set pixel at (x, y) when all you want to do is change the color"""
        current_pixel: RGBPixel = self.pixels[y][x]
        self.set_px(RGBPixel(RGBColor(*color), current_pixel.symbol), x, y)

    def fill(self, color: Tuple[int, int, int]) -> Screen:
        for x in range(self.width):
            for y in range(self.height):
                self.set_px(RGBPixel(RGBColor(*color)), x, y)

        return self

    def paint_image(
        self,
        image: np.ndarray | str,
        x: int = 0,
        y: int = 0,
        has_alpha: bool = False,
        resize: Tuple[int, int] = None,
    ) -> Screen:
        """
        Paint an image on the screen (can be a path to an image or a numpy array).
        Resize the image to the given size if resize is not None.
        """

        # load and resize image if it is a string
        if isinstance(image, str):
            image = Image.open(image).convert("RGB" if not has_alpha else "RGBA")
            image = np.array(image)

        if resize:
            image = Image.fromarray(image).resize(resize)
            image = np.array(image)

        if image.shape[2] < 3:
            raise ValueError("Image must have at least 3 channels")

        image_width = image.shape[1]
        image_height = image.shape[0]

        if image_height + y > self.height or image_width + x > self.width:
            raise ValueError(
                "The image is too big for the screen at this position. Image size:"
                f" ({image.shape[1]}, {image.shape[0]}) Screen size:({self.width},"
                f" {self.height})\nEither use a bigger screen, or call Screen.from_image."
            )

        for image_x in range(image.shape[1]):
            for image_y in range(image.shape[0]):

                px = RGBPixel(RGBColor(*image[image_y][image_x][:3]))

                # ignore transparent pixels
                if has_alpha and image[image_y][image_x][3] == 0:
                    px.transparent = True

                self.set_px(px, x + image_x, y + image_y)

        return self

    @staticmethod
    def from_image(
        image: np.ndarray | str,
        resize: Tuple[int, int] | None = None,
        has_alpha: bool = False,
    ) -> Screen:
        """
        Create a screen from an image (can be a path to an image or a numpy array).\n
        If resize is not None, the image will be resized to the given size.
        """

        if isinstance(image, str):
            image = Image.open(image).convert("RGB" if not has_alpha else "RGBA")
        else:
            image = Image.fromarray(image)

        if resize is not None:
            image = image.resize(resize)

        image = np.array(image)

        image_width = image.shape[1]
        image_height = image.shape[0]

        return Screen(image_width, image_height).paint_image(image, has_alpha=has_alpha)

    def __check_coordinate(self, x: int, y: int) -> bool:
        return (0 <= x < self.width) and (0 <= y < self.height)

    def paint_screen(self, screen: Screen, x: int, y: int) -> Screen:
        """Paint another screen onto the screen at the given coordinates"""

        for xi in range(screen.width):
            for yi in range(screen.height):

                # ignore transparent pixels
                if screen.pixels[yi][xi].transparent:
                    continue

                self.set_px(screen.pixels[yi][xi], xi + x, yi + y)

        return self

    def clear(self) -> None:
        self.pixels = np.array(
            [
                [RGBPixel(transparent=True) for _ in range(self.width)]
                for _ in range(self.height)
            ]
        )

    def render(self) -> None:
        """
        Render the screen and print it to stdout
        """
        for row_i in range(self.height):
            row = self.pixels[row_i]
            pixel: RGBPixel
            for pixel in row:
                print(pixel, end="")
            print()

    def __str__(self) -> str:
        return f"Screen ({self.width}, {self.height})"

    __repr__ = __str__
