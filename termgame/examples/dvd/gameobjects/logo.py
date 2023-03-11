from __future__ import annotations

import os
from random import randint

import pymunk

from termgame import PhysicsGameobject, Screen
from termgame.util import stretch_animation


class DVDLogo(PhysicsGameobject):

    SPRITES_FOLDER = os.path.dirname(os.path.abspath(__file__)) + "/../sprites/"
    DVD_SIZE = (16, 8)

    def __init__(self):

        sprites = stretch_animation(
            [
                Screen.from_image(DVDLogo.SPRITES_FOLDER + "dvd.png", resize=DVDLogo.DVD_SIZE),
                Screen.from_image(
                    DVDLogo.SPRITES_FOLDER + "dvd_yellow.png", resize=DVDLogo.DVD_SIZE
                ),
            ],
            randint(1, 5),
        )

        PhysicsGameobject.__init__(
            self, sprites=sprites, x=0, y=0, name="DVD Logo", on_start=self.on_start
        )  # , on_update=self.bounce

    def on_start(self, engine):
        c = pymunk.Poly(
            self.rb,
            [
                (0, 0),
                (self.width, 0),
                (self.width, self.height),
                (0, self.height),
            ],
        )
        c.mass = 1
        engine.space.add(c)

    # def randomize_pos(self: DVDLogo, engine):
    #     self.x = choice(range(engine.width - self.width))
    #     self.y = choice(range(engine.height - self.height))

    # def bounce(self, frame, engine):

    #     # define directions
    #     dirs = {
    #         "up": (0, -1),
    #         "down": (0, 1),
    #         "left": (-1, 0),
    #         "right": (1, 0),
    #         "upleft": (-1, -1),
    #         "upright": (1, -1),
    #         "downleft": (-1, 1),
    #         "downright": (1, 1),
    #     }

    #     def apply_dir(dir: str) -> None:
    #         self.state["dir"] = dir
    #         self.x += dirs[dir][0]
    #         self.y += dirs[dir][1]

    #     w = engine.width
    #     h = engine.height

    #     # check if the gameobject is at the edge of the screen and choose a bounce direction
    #     sprite_width: int = self.width
    #     sprite_height: int = self.height

    #     on_left = lambda go: go.x == 0
    #     on_right = lambda go: go.x + sprite_width == w
    #     on_top = lambda go: go.y == 0
    #     on_bottom = lambda go: go.y + sprite_height == h

    #     # initialize movement with random direction
    #     if "dir" not in self.state:
    #         apply_dir(
    #             choice(
    #                 ["downright", "downleft", "upright", "upleft", "down", "right", "left", "up"]
    #             )
    #         )

    #     if self.state["dir"] == "right":
    #         if on_right(self) and on_top(self):
    #             apply_dir(choice(["down", "left", "downleft"]))
    #         elif on_right(self) and on_bottom(self):
    #             apply_dir(choice(["up", "left", "upleft"]))
    #         elif on_right(self):
    #             apply_dir(choice(["up", "down", "left", "upleft", "downleft"]))
    #         else:
    #             apply_dir("right")
    #     elif self.state["dir"] == "left":
    #         if on_left(self) and on_top(self):
    #             apply_dir(choice(["down", "right", "downright"]))
    #         elif on_left(self) and on_bottom(self):
    #             apply_dir(choice(["up", "right", "upright"]))
    #         elif on_left(self):
    #             apply_dir(choice(["up", "down", "right", "upright", "downright"]))
    #         else:
    #             apply_dir("left")
    #     elif self.state["dir"] == "up":
    #         if on_top(self) and on_left(self):
    #             apply_dir(choice(["down", "right", "downright"]))
    #         elif on_top(self) and on_right(self):
    #             apply_dir(choice(["down", "left", "downleft"]))
    #         elif on_top(self):
    #             apply_dir(choice(["down", "left", "right", "downleft", "downright"]))
    #         else:
    #             apply_dir("up")
    #     elif self.state["dir"] == "down":
    #         if on_bottom(self) and on_left(self):
    #             apply_dir(choice(["up", "right", "upright"]))
    #         elif on_bottom(self) and on_right(self):
    #             apply_dir(choice(["up", "left", "upleft"]))
    #         elif on_bottom(self):
    #             apply_dir(choice(["up", "left", "right", "upleft", "upright"]))
    #         else:
    #             apply_dir("down")
    #     elif self.state["dir"] == "upleft":
    #         if on_top(self) and on_left(self):
    #             apply_dir(choice(["down", "right", "downright"]))
    #         elif on_top(self):
    #             apply_dir(choice(["down", "right", "downright", "downleft"]))
    #         elif on_left(self):
    #             apply_dir(choice(["down", "up", "right", "downright", "upright"]))
    #         else:
    #             apply_dir("upleft")
    #     elif self.state["dir"] == "upright":
    #         if on_top(self) and on_right(self):
    #             apply_dir(choice(["down", "left", "downleft"]))
    #         elif on_top(self):
    #             apply_dir(choice(["down", "left", "downleft", "downright"]))
    #         elif on_right(self):
    #             apply_dir(choice(["down", "up", "left", "downleft", "upleft"]))
    #         else:
    #             apply_dir("upright")
    #     elif self.state["dir"] == "downleft":
    #         if on_bottom(self) and on_left(self):
    #             apply_dir(choice(["up", "right", "upright"]))
    #         elif on_bottom(self):
    #             apply_dir(choice(["up", "right", "upright", "upleft"]))
    #         elif on_left(self):
    #             apply_dir(choice(["up", "down", "right", "upright", "downright"]))
    #         else:
    #             apply_dir("downleft")
    #     elif self.state["dir"] == "downright":
    #         if on_bottom(self) and on_right(self):
    #             apply_dir(choice(["up", "left", "upleft"]))
    #         elif on_bottom(self):
    #             apply_dir(choice(["up", "left", "upleft", "upright"]))
    #         elif on_right(self):
    #             apply_dir(choice(["up", "down", "left", "upleft", "downleft"]))
    #         else:
    #             apply_dir("downright")
