import pymunk

from termgame import Engine, PhysicsGameobject, Screen
from termgame.util import get_bb_poly


class Wall(PhysicsGameobject):
    def __init__(self, x, y, w, h):
        sprites = [Screen(w, h).fill((128, 128, 128))]
        PhysicsGameobject.__init__(
            self,
            x=x,
            y=y,
            sprites=sprites,
            on_update=self.on_update,
            on_start=self.on_start,
            static_body=True,
            name="Wall",
            
        )

    def on_start(self, engine: Engine):
        c = get_bb_poly(self)
        c.elasticity = 0.9
        c.mass = 1
        engine.space.add(c)

    def on_update(self, frame, engine: Engine):
        pass
