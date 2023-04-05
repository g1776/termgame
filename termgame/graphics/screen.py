"""
Description: Define the Screen class.
Author: Gregory Glatzer
Date: 10/22/2022
"""

from __future__ import annotations

from typing import Tuple

import numpy as np
from PIL import Image  # type: ignore

from .pixel import RGBColor, RGBPixel


class Screen:
    def __init__(self, width: int, height: int):
        """
        Initialize a new Screen object with a given width and height.

        :param width: Width of the screen.
        :type width: int
        :param height: Height of the screen.
        :type height: int
        """
        self.width = width
        self.height = height
        # define the screen as a cleared screen (all pixels are black)
        self.clear()

    def set_px(self, px: RGBPixel, x: int, y: int) -> Screen:
        """
        Set pixel at (x,y) on the screen to a new pixel.

        :param px: RGBPixel object to be set on the screen.
        :type px: RGBPixel
        :param x: x-coordinate of the pixel on the screen.
        :type x: int
        :param y: y-coordinate of the pixel on the screen.
        :type y: int
        :return: Screen object with updated pixel.
        :rtype: Screen
        """
        self.__check_coordinate(x, y)
        self.pixels[y][x] = px
        return self

    def set_px_color(self, color: Tuple[int, int, int], x: int, y: int) -> Screen:
        """
        Shorthand to set pixel at (x, y) when all you want to do is change the color.

        :param color: Tuple of three integers (R,G,B) representing the color of the pixel.
        :type color: Tuple[int, int, int]
        :param x: x-coordinate of the pixel on the screen.
        :type x: int
        :param y: y-coordinate of the pixel on the screen.
        :type y: int
        :return: Screen object with updated pixel.
        :rtype: Screen
        """
        current_pixel: RGBPixel = self.pixels[y][x]
        self.set_px(RGBPixel(RGBColor(*color), current_pixel.symbol), x, y)

        return self

    def fill(self, color: Tuple[int, int, int]) -> Screen:
        """
        Fill the entire screen with a given color.

        :param color: Tuple of three integers (R,G,B) representing the color of the pixel.
        :type color: Tuple[int, int, int]
        :return: Screen object with updated pixels.
        :rtype: Screen
        """
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

        :param image: Path to an image or a numpy array.
        :type image: np.ndarray | str
        :param x: x-coordinate of the top-left corner of the image on the screen. Default is 0.
        :type x: int
        :param y: y-coordinate of the top-left corner of the image on the screen. Default is 0.
        :type y: int
        :param has_alpha: Whether the image has an alpha channel
        :param resize: Resize the image to the given size
        :type resize: Tuple[int, int]
        :return: Screen object with updated pixels.
        :rtype: Screen
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
        image: np.ndarray | str, resize: Tuple[int, int] | None = None, has_alpha: bool = False
    ) -> Screen:
        """
        Create a screen from an image (can be a path to an image or a numpy array).
        If resize is not None, the image will be resized to the given size.

        :param image: The image to create the screen from.
        :type image: numpy.ndarray | str
        :param resize: The size to resize the image to.
        :type resize: tuple[int, int] | None
        :param has_alpha: A boolean indicating whether the image has an alpha channel.
        :type has_alpha: bool
        :return: The screen created from the image.
        :rtype: Screen
        """
        if isinstance(image, str):
            img: Image = Image.open(image).convert("RGB" if not has_alpha else "RGBA")  # type: ignore
        else:
            img: Image = Image.fromarray(image)  # type: ignore

        if resize is not None:
            img = img.resize(resize)  # type: ignore

        img = np.array(img)  # type: ignore

        image_width = img.shape[1]
        image_height = img.shape[0]

        return Screen(image_width, image_height).paint_image(img, has_alpha=has_alpha)

    def __check_coordinate(self, x: int, y: int) -> bool:
        """
        Check if the given coordinates are within the bounds of the screen.

        :param x: The x-coordinate to check.
        :type x: int
        :param y: The y-coordinate to check.
        :type y: int
        :return: A boolean indicating whether the coordinates are within the bounds of the screen.
        :rtype: bool
        """
        return (0 <= x < self.width) and (0 <= y < self.height)

    def paint_screen(self, screen: Screen, x: int, y: int) -> Screen:
        """
        Paint another screen onto the screen at the given coordinates.

        :param screen: The screen to paint onto this screen.
        :type screen: Screen
        :param x: The x-coordinate to paint the screen.
        :type x: int
        :param y: The y-coordinate to paint the screen.
        :type y: int
        :return: The resulting screen after painting the other screen onto this screen.
        :rtype: Screen
        """
        for xi in range(screen.width):
            for yi in range(screen.height):

                # ignore transparent pixels
                if screen.pixels[yi][xi].transparent:
                    continue

                self.set_px(screen.pixels[yi][xi], xi + x, yi + y)

        return self

    def clear(self) -> None:
        """
        Clear the screen by setting all pixels to transparent Pixels with no color.

        :return: None
        """
        self.pixels = np.array(
            [[RGBPixel(transparent=True) for _ in range(self.width)] for _ in range(self.height)]
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
