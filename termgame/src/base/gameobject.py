"""
Description: The game object class.
Author: Gregory Glatzer
Date: 10/23/2022
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, List, Dict, Any
from ..util import clamp


@dataclass
class Gameobject:
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        depth: int = 0,
        update_order: int = 0,
        sprites: List | None = None,
        on_start: Callable = lambda engine: None,
        on_update: Callable = lambda frame, engine: None,
        name: str = "",
    ):
        self.x = x
        self.y = y
        self.depth = depth
        self.update_order = update_order
        self.sprites = sprites
        self.state: Dict[Any, Any] = {}
        self.__name = name
        self.__active_sprite_idx = None

        def internal_on_update(frame: int, engine):
            """Some things we want to do every frame on top of what the developer wants."""

            # Move the animation to the next frame in the list of sprites.
            if (self.sprites is not None) and (len(self.sprites) > 0):
                self.__active_sprite_idx = frame % len(self.sprites)

            # this is a hack to make sure the object always stays within the screen.
            # TODO: fix this.
            self.x = clamp(self.x, 0, engine.width - self.width)
            self.y = clamp(self.y, 0, engine.height - self.height)

            # call the developer's on_update function.
            on_update(frame, engine)

        def internal_on_start(engine):
            """Some things we want to do when the gameobject is added to the engine."""
            if (self.sprites is not None) and (len(self.sprites) > 0):
                self.__active_sprite_idx = 0
            on_start(engine)

        self.on_update = internal_on_update
        self.on_start = internal_on_start

    def get_active_sprite(self):
        if self.__active_sprite_idx is None:
            return None
        return self.sprites[self.__active_sprite_idx]

    @property
    def name(self) -> str:
        return self.__name

    @property
    def has_physics(self) -> bool:
        return False

    @property
    def width(self) -> int:
        active_sprite = self.get_active_sprite()
        if active_sprite is None:
            return 0
        return active_sprite.width

    @property
    def height(self) -> int:
        active_sprite = self.get_active_sprite()
        if active_sprite is None:
            return 0
        return active_sprite.height

    def __str__(self):
        return f"Gameobject({self.name})"

    __repr__ = __str__
