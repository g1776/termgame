import random

from termgame import Gameobject


class WaveManager(Gameobject):
    def __init__(self):
        Gameobject.__init__(
            self,
            name="WaveManager",
            on_update=self.on_update,
            on_start=self.on_start,
            update_order=-1,
        )

    def on_start(self, engine):
        engine.state["wave"] = False
        engine.state["force"] = (0, 0)

    def on_update(self, frame, engine):

        # turn wave off if it is on
        if engine.state["wave"]:
            engine.state["wave"] = False

        # Turn wave on at chance of 10%
        if random.randint(0, 100) > 90:
            engine.state["wave"] = True
            force_x = engine.space.gravity[1] * random.randint(-20, 20)
            force_y = engine.space.gravity[1] * random.randint(0, 20)
            force = (force_x, force_y)
            engine.state["force"] = force
