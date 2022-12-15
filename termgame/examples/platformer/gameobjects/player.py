import os

import keyboard

from termgame import Engine, PhysicsGameobject, Screen
from termgame.util import flip_animation, get_bb_poly, stretch_animation


class Player(PhysicsGameobject):

    PLAYER_SIZE = (7, 8)
    SPRITES_FOLDER = os.path.dirname(os.path.abspath(__file__)) + "/../sprites/player/"

    def __init__(self, screen_height):

        ground_height = 1

        self.walk_right = stretch_animation(
            [
                Screen.from_image(self.SPRITES_FOLDER + "walk1.png", has_alpha=True),
                Screen.from_image(self.SPRITES_FOLDER + "walk2.png", has_alpha=True),
                Screen.from_image(self.SPRITES_FOLDER + "walk3.png", has_alpha=True),
            ],
            3,
        )

        self.walk_left = flip_animation(self.walk_right, "x")

        PhysicsGameobject.__init__(
            self,
            x=0,
            y=screen_height - ground_height - Player.PLAYER_SIZE[1] - 5,
            sprites=self.walk_right,
            on_start=self.on_start,
            on_fixed_update=self.on_fixed_update,
            name="Player",
        )

    def on_start(self, engine):
        self.sprites = self.walk_right
        self.jumping = False

        c = get_bb_poly(self)
        c.mass = 1
        engine.space.add(c)

    def on_fixed_update(self, frame, engine):

        if keyboard.is_pressed("right"):
            self.sprites = self.walk_right
            if self.x <= engine.width - Player.PLAYER_SIZE[0]:
                self.rb.position = (self.x + 1, self.y)
        elif keyboard.is_pressed("left"):
            self.sprites = self.walk_left
            if self.x >= 0:
                self.rb.position = (self.x - 1, self.y)
