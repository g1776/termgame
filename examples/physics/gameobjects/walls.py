from termgame import PhysicsGameobject, Engine, Screen
import pymunk


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

        c = pymunk.Poly(
            self.rb,
            [
                (0, 0),
                (self.width, 0),
                (self.width, self.height),
                (0, self.height),
            ],
        )
        c.elasticity = 0.9
        c.mass = 1
        engine.space.add(c)

    def on_update(self, frame, engine: Engine):
        pass
