"""
Description: Wrapper around the base engine to add physics with pymunk.
Author: Gregory Glatzer
Date: 12/12/2022
"""

from typing import List, cast

import pymunk

from ..logger import Logger
from ..util import get_bb_poly
from .engine import Engine
from .gameobject import Gameobject
from .physics_gameobject import PhysicsGameobject


class PhysicsEngine(Engine):
    def __init__(
        self,
        width: int,
        height: int,
        gravity: tuple[float, float] = (0, 98.1),
        **engine_kwargs,
    ):
        """A wrapper around the base engine to add physics with pymunk.

        Args:
            width (int): Screen Width
            height (int): Screen Height
            gravity (tuple[int, int], optional): The gravity for the physics simulation.
                Use 98.1, not 9.8. Defaults to (0, 98.1).
        """

        self.__space = pymunk.Space()
        self.__space.gravity = gravity
        super().__init__(width, height, **engine_kwargs)

    def add_gameobject(self, gameobject: Gameobject) -> None:
        """
        Add a gameobject to the engine. Will also add the rigidbody
            to the physics space, if it has one.
        """

        # this will be the collision shape for the static gameobject, if we end up making one.
        shape = None

        if not isinstance(gameobject, PhysicsGameobject):
            Logger.info(
                (
                    "Can only add PhysicsGameobjects to PhysicsEngine. %s -> STATIC"
                    " rigidbody with Poly shape."
                ),
                gameobject,
            )
            # if the gameobject doesn't have a rigidbody, add a static one to the space.
            gameobject = PhysicsGameobject.from_gameobject(gameobject, static_body=True)
            shape = get_bb_poly(gameobject)

        super().add_gameobject(gameobject)
        if shape is not None:
            self.__space.add(gameobject.rb, shape)
        else:
            self.__space.add(gameobject.rb)

    @property
    def space(self) -> pymunk.Space:
        """The pymunk space for 2d physics."""
        return self.__space

    def run(self, fps: int, headless: bool = False, ppf: int = 5) -> None:
        def runtime_injection(self: PhysicsEngine):
            """This function is injected into the base engine's run function.
                It is called every frame.

            Args:
                self (PhysicsEngine): The engine.
                fps (int): The frames per second.
                ppf (int, optional): Physics Per Frame. This defines the number of physics
                    simulations per frame, ie how many times "fixed_update()"
                    is called per frame. Defaults to 5.
            """
            for _ in range(ppf):
                self.space.step(1 / (fps * ppf))

            gos_in_call_order = sorted(
                cast(List[PhysicsGameobject], self.gameobjects),
                key=lambda go: go.update_order,
            )
            for gameobject in gos_in_call_order:
                gameobject.on_fixed_update(self.frame, self)

        self._run(fps, runtime_injection, headless)
