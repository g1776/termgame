from __future__ import annotations

from typing import Callable

import pymunk

from ..logger import Logger
from ..util import clamp
from .gameobject import Gameobject


class PhysicsGameobject(Gameobject):
    def __init__(
        self,
        on_fixed_update: Callable = lambda frame, engine: None,
        static_body: bool = False,
        max_velocity: int = None,
        **gameobject_kwargs,
    ):

        super().__init__(**gameobject_kwargs)

        self.__rigidbody = pymunk.Body(
            body_type=pymunk.Body.STATIC if static_body else pymunk.Body.DYNAMIC
        )
        self.__rigidbody.position = (self.x, self.y)

        if max_velocity is not None:

            def limit_velocity(body, gravity, damping, dt):
                pymunk.Body.update_velocity(body, gravity, damping, dt)
                body_length = body.velocity.length
                if body_length > max_velocity:
                    scale = max_velocity / body_length
                    body.velocity = body.velocity * scale

            self.__rigidbody.velocity_func = limit_velocity

        def internal_on_fixed_update(frame: int, engine):
            """Some things we want to do every fixed frame on top of what the
            developer wants, after the physics engine has updated."""

            if len(self.__rigidbody.shapes) == 0:
                Logger.warning(
                    (
                        "%s has no shapes attached to its rigidbody. This may result in errors"
                        " and unexpected behavior."
                    ),
                    self,
                )

            try:
                # Update the position of the gameobject to match the rigidbody.
                self.x = round(self.__rigidbody.position.x)
                self.y = round(self.__rigidbody.position.y)
            except ValueError:
                # if position is NaN for some reason, do not update position.
                on_fixed_update(frame, engine)
                return

            # this is a hack to make sure the object always stays within the screen.
            # TODO: fix this.
            self.x = clamp(self.x, 0, engine.width - self.width)
            self.y = clamp(self.y, 0, engine.height - self.height)

            # call the developer's on_fixed_update function.
            on_fixed_update(frame, engine)

        self.on_fixed_update = internal_on_fixed_update

    @property
    def has_physics(self) -> bool:
        return True

    @property
    def rigidbody(self) -> pymunk.Body:
        return self.__rigidbody

    @property
    def rb(self) -> pymunk.Body:
        """Shorthand for self.rigidbody"""
        return self.__rigidbody

    def _set_rb(self, value: pymunk.Body):
        """Be careful using this. It will replace the gameobject's rigidbody."""
        self.__rigidbody = value

    @staticmethod
    def from_gameobject(gameobject: Gameobject, static_body: bool = True) -> PhysicsGameobject:
        """Convert a Gameobject to a PhysicsGameobject."""
        return PhysicsGameobject(
            x=gameobject.x,
            y=gameobject.y,
            depth=gameobject.depth,
            sprites=gameobject.get_sprites(),
            on_start=gameobject.on_start,
            on_update=gameobject.on_update,
            name=gameobject.name,
            static_body=static_body,
        )
