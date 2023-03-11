"""
Description: This module contains utility functions for termgame.
Author: Gregory Glatzer
Date: 11/07/2022
"""

from __future__ import annotations
import numpy as np
import pymunk

from typing import List
from .graphics.screen import Screen
from ctypes import POINTER, WinDLL, Structure, sizeof, byref
from ctypes.wintypes import BOOL, SHORT, WCHAR, UINT, ULONG, DWORD, HANDLE


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


def get_bb_poly(go) -> pymunk.Poly:
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


def change_font_size(size=2):

    LF_FACESIZE = 32
    STD_OUTPUT_HANDLE = -11

    class COORD(Structure):
        _fields_ = [
            ("X", SHORT),
            ("Y", SHORT),
        ]

    class CONSOLE_FONT_INFOEX(Structure):
        _fields_ = [
            ("cbSize", ULONG),
            ("nFont", DWORD),
            ("dwFontSize", COORD),
            ("FontFamily", UINT),
            ("FontWeight", UINT),
            ("FaceName", WCHAR * LF_FACESIZE),
        ]

    kernel32_dll = WinDLL("kernel32.dll")

    get_last_error_func = kernel32_dll.GetLastError
    get_last_error_func.argtypes = []
    get_last_error_func.restype = DWORD

    get_std_handle_func = kernel32_dll.GetStdHandle
    get_std_handle_func.argtypes = [DWORD]
    get_std_handle_func.restype = HANDLE

    get_current_console_font_ex_func = kernel32_dll.GetCurrentConsoleFontEx
    get_current_console_font_ex_func.argtypes = [HANDLE, BOOL, POINTER(CONSOLE_FONT_INFOEX)]
    get_current_console_font_ex_func.restype = BOOL

    set_current_console_font_ex_func = kernel32_dll.SetCurrentConsoleFontEx
    set_current_console_font_ex_func.argtypes = [HANDLE, BOOL, POINTER(CONSOLE_FONT_INFOEX)]
    set_current_console_font_ex_func.restype = BOOL

    stdout = get_std_handle_func(STD_OUTPUT_HANDLE)
    font = CONSOLE_FONT_INFOEX()
    font.cbSize = sizeof(CONSOLE_FONT_INFOEX)

    font.dwFontSize.X = size
    font.dwFontSize.Y = size

    set_current_console_font_ex_func(stdout, False, byref(font))
