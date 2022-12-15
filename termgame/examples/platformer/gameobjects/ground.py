import os

import pymunk

from termgame import PhysicsGameobject, Screen


class Ground(PhysicsGameobject):
    SPRITES_FOLDER = os.path.dirname(os.path.abspath(__file__)) + "/../sprites/"

    def __init__(self, x, y, width, height):

        sprites = [Screen(width, height).fill((196, 112, 6))]

        PhysicsGameobject.__init__(self, x=x, y=y, sprites=sprites, static_body=True)

    def on_start(self, engine):
        c = pymunk.Poly(
            self.rb,
            [(0, 0), (self.width, 0), (self.width, self.height), (0, self.height)],
        )
        c.mass = 1
        engine.space.add(c)
