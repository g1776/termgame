from termgame import PhysicsGameobject, PhysicsEngine, Screen
import pymunk


class Particle(PhysicsGameobject):
    def __init__(self, x, y, color):
        sprites = [Screen(1, 1).fill(color)]
        PhysicsGameobject.__init__(
            self,
            x=x,
            y=y,
            sprites=sprites,
            on_fixed_update=self.on_fixed_update,
            on_start=self.on_start,
            name="Particle",
        )

    def on_start(self, engine: PhysicsEngine):

        c = pymunk.Circle(self.rb, 0.75)
        c.mass = 10
        c.elasticity = 0.5
        engine.space.add(c)

    def on_fixed_update(self, frame, engine: PhysicsEngine):
        if engine.state["wave"]:
            force = engine.state["force"]
            self.rb.apply_impulse_at_local_point(force)
