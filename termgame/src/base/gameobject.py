"""
Description: The game object class.
Author: Gregory Glatzer
Date: 10/23/2022
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, List, Dict, Any


class GameobjectAnimator:
    """Class for animating gameobjects by looping through a list of sprites or meshes."""

    def __init__(self, elements: List):
        self.elements = elements
        self.active_el_idx = None

    def start(self) -> None:
        """Start the animation."""
        if self.elements != []:
            self.active_el_idx = 0

    def next(self, frame: int) -> None:
        """Move the animation to the next frame in the list of elements."""
        if self.elements != []:
            self.active_el_idx = frame % len(self.elements)

    def get_active_element(self) -> Any:
        if self.active_el_idx is None:
            return None
        return self.elements[self.active_el_idx]


@dataclass
class Gameobject:
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        depth: int = 0,
        update_order: int = 0,
        sprites: List | None = None,
        meshes: List | None = None,
        on_start: Callable = lambda engine: None,
        on_update: Callable = lambda frame, engine: None,
        name: str = "",
    ):
        self.x = x
        self.y = y
        self.depth = depth
        self.update_order = update_order

        # make sure the developer doesn't try to use both sprites and meshes.
        if (sprites is not None) and (meshes is not None):
            raise ValueError("Cannot use both sprites and meshes.")
        self.__animator = GameobjectAnimator((sprites or meshes) or [])

        self.state: Dict[Any, Any] = {}
        self.__name = name

        def internal_on_update(frame: int, engine):
            """Some things we want to do every frame on top of what the developer wants."""

            # update the active sprite/mesh.
            self.__animator.next(frame)

            # call the developer's on_update function.
            on_update(frame, engine)

        def internal_on_start(engine):
            """Some things we want to do when the gameobject is added to the engine."""

            # start the animator.
            self.__animator.start()

            on_start(engine)

        self.on_update = internal_on_update
        self.on_start = internal_on_start

    @property
    def name(self) -> str:
        return self.__name

    @property
    def has_physics(self) -> bool:
        return False

    @property
    def width(self) -> int | float:
        active_element = self.__animator.get_active_element()
        if active_element is None:
            return 0
        return active_element.width

    @property
    def height(self) -> int | float:
        active_element = self.__animator.get_active_element()
        if active_element is None:
            return 0
        return active_element.height

    def get_sprites(self) -> Any:
        """Access the sprites (2D) of the gameobject, if any."""
        return self.__animator.elements

    def set_sprites(self, sprites) -> None:
        self.__animator = GameobjectAnimator(sprites)
        self.__animator.start()
        return None

    def get_active_sprite(self) -> Any:
        """Access the active sprite (2D) of the gameobject, if any."""
        return self.__animator.get_active_element()

    def get_meshes(self) -> Any:
        """Access the meshes (3D) of the gameobject, if any."""
        return self.__animator.elements

    def set_meshes(self, meshes) -> None:
        self.__animator = GameobjectAnimator(meshes)
        self.__animator.start()
        return None

    def get_active_mesh(self) -> Any:
        """Access the active mesh (3D) of the gameobject, if any."""
        return self.__animator.get_active_element()

    def __str__(self):
        return f"Gameobject({self.name})"

    __repr__ = __str__
