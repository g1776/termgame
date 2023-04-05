"""
Description: This module contains utility functions for termgame.
Author: Gregory Glatzer
Date: 4/04/2023
"""

from __future__ import annotations
from typing import Any, List
import numpy as np
import pymunk

from .graphics.screen import Screen


def stretch_animation(sprites: List[Screen], stretch: int):
    """
    Stretch an animation out (multiply frames). This effectively slows down the animation.

    :param sprites: List of sprites to stretch.
    :type sprites: List[Screen]
    :param stretch: Number of times to stretch the animation.
    :type stretch: int
    :return: List of stretched sprites.
    :rtype: List[Screen]
    """

    new_sprites = []
    for sprite in sprites:
        for _ in range(stretch):
            new_sprites.append(sprite)
    return new_sprites


def flip_animation(sprites: List[Screen], axis: str = "x") -> List[Screen]:
    """
    Flip an animation along the given axis (x or y).

    :param sprites: List of sprites to flip.
    :type sprites: List[Screen]
    :param axis: Axis to flip the animation along, either x or y.
    :type axis: str
    :return: List of flipped sprites.
    :rtype: List[Screen]
    """

    if axis not in ["x", "y"]:
        raise ValueError("axis must be either x or y")

    new_sprites: List[Screen] = []
    for sprite in sprites:
        new_sprite: Screen = Screen(sprite.width, sprite.height).paint_screen(sprite, 0, 0)
        new_sprite.pixels = np.flip(new_sprite.pixels, axis=0 if axis == "y" else 1)
        new_sprites.append(new_sprite)
    return new_sprites


def scroll_sprite(sprite: Screen, dx: int, dy: int) -> Screen:
    """
    Scroll a sprite by dx and dy.

    :param sprite: Sprite to scroll.
    :type sprite: Screen
    :param dx: Number of pixels to scroll in the x direction.
    :type dx: int
    :param dy: Number of pixels to scroll in the y direction.
    :type dy: int
    :return: Scrolled sprite.
    :rtype: Screen
    """

    new_sprite: Screen = Screen(sprite.width, sprite.height).paint_screen(sprite, 0, 0)
    new_sprite.pixels = np.roll(new_sprite.pixels, dx, axis=1)
    new_sprite.pixels = np.roll(new_sprite.pixels, dy, axis=0)
    return new_sprite


def get_bb_poly(go) -> pymunk.Poly:
    """
    Get a polygon for a gameobject to be used pymunk shape
    that is a rectangle the width and height of the gameobject.

    :param go: Gameobject to get the bounding box for.
    :type go: GameObject
    :return: pymunk.Poly object representing the bounding box.
    :rtype: pymunk.Poly
    """

    return pymunk.Poly(
        go.rigidbody,
        [
            (0, 0),
            (go.width, 0),
            (go.width, go.height),
            (0, go.height),
        ],
    )


def clamp(value: Any, smallest: Any, largest: Any) -> Any:
    return max(smallest, min(value, largest))
