import os

import pymunk

from termgame import PhysicsGameobject, Screen
from termgame.util import get_bb_poly


class Ground(PhysicsGameobject):
    SPRITES_FOLDER = os.path.dirname(os.path.abspath(__file__)) + "/../sprites/"

    def __init__(self, x, y, width, height):

        sprites = [Screen(width, height).fill((196, 112, 6))]

        PhysicsGameobject.__init__(
            self,
            x=x,
            y=y,
            sprites=sprites,
            static_body=True,
            on_start=self.on_start,
            name="Ground",
        )

    def on_start(self, engine):
        c = get_bb_poly(self)
        c.mass = 1
        engine.space.add(c)
