"""
Description: This module contains utility functions for termgame.
Author: Gregory Glatzer
Date: 11/07/2022
"""

from typing import List

import numpy as np
import pymunk

from .base import PhysicsGameobject
from .graphics.screen import Screen


def stretch_animation(sprites: List[Screen], stretch: int):
    """
    Stretch an animation out (multiply frames). This effectively slows down the animation.
    """

    new_sprites = []
    for sprite in sprites:
        for _ in range(stretch):
            new_sprites.append(sprite)
    return new_sprites


def flip_animation(sprites: List[Screen], axis: str = "x"):
    """
    Flip an animation along the given axis (x or y).
    """

    if axis not in ["x", "y"]:
        raise ValueError("axis must be either x or y")

    new_sprites = []
    for sprite in sprites:
        new_sprite: Screen = Screen(sprite.width, sprite.height).paint_screen(sprite, 0, 0)
        new_sprite.pixels = np.flip(new_sprite.pixels, axis=0 if axis == "y" else 1)
        new_sprites.append(new_sprite)
    return new_sprites


def scroll_sprite(sprite: Screen, dx: int, dy: int) -> Screen:
    """
    Scroll a sprite by dx and dy.
    """

    new_sprite: Screen = Screen(sprite.width, sprite.height).paint_screen(sprite, 0, 0)
    new_sprite.pixels = np.roll(new_sprite.pixels, dx, axis=1)
    new_sprite.pixels = np.roll(new_sprite.pixels, dy, axis=0)
    return new_sprite


def get_bb_poly(go: PhysicsGameobject) -> pymunk.Poly:
    """
    Get a polygon for a gameobject to be used pymunk shape
    that is a rectangle the width and height of the gameobject.
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


def clamp(value, smallest, largest):
    return max(smallest, min(value, largest))
