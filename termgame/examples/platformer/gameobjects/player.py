import os

import keyboard

from termgame import PhysicsGameobject, Screen
from termgame.util import flip_animation, get_bb_poly, stretch_animation


class Player(PhysicsGameobject):

    PLAYER_SIZE = (7, 8)
    SPRITES_FOLDER = os.path.dirname(os.path.abspath(__file__)) + "/../sprites/player/"
    RUNNING_FORCE = 50
    JUMP_FORCE = 3

    def __init__(self, screen_height, ground_height, lru=["left", "right", "up"], name="Player 1"):

        self.lru = lru

        # State
        self.pressed = False

        # animations
        self.stand = [
            Screen.from_image(Player.SPRITES_FOLDER + "walk1.png", has_alpha=True),
        ]
        self.walk_right_animation = stretch_animation(
            [
                Screen.from_image(Player.SPRITES_FOLDER + "walk1.png", has_alpha=True),
                Screen.from_image(Player.SPRITES_FOLDER + "walk2.png", has_alpha=True),
                Screen.from_image(Player.SPRITES_FOLDER + "walk3.png", has_alpha=True),
            ],
            3,
        )
        self.walk_left_animation = flip_animation(self.walk_right_animation, "x")

        PhysicsGameobject.__init__(
            self,
            x=0,
            y=screen_height - ground_height - Player.PLAYER_SIZE[1],
            sprites=self.walk_right_animation,
            on_start=self.on_start,
            on_fixed_update=self.on_fixed_update,
            name=name,
            max_velocity=30,
        )

    def on_start(self, engine):

        c = get_bb_poly(self)
        c.mass = 10
        engine.space.add(c)

    def walk_right(self, engine):

        # we don't want to glide, so cancel out any horizontal motion
        if self.rb.velocity[0] < 0.00:
            self.rb._set_velocity((0.00, self.rb.velocity[1]))

        if not self.pressed:
            self.pressed = True
            self.set_sprites(self.walk_right_animation)
        if self.x <= engine.width - Player.PLAYER_SIZE[0]:
            walk_impulse = (Player.RUNNING_FORCE, 0)
            center = (self.width // 2, self.height // 2)
            self.rb.apply_impulse_at_local_point(walk_impulse, center)

    def walk_left(self):

        # we don't want to glide, so cancel out any horizontal motion
        if self.rb.velocity[0] > 0.00:
            self.rb._set_velocity((0.00, self.rb.velocity[1]))

        if not self.pressed:
            self.pressed = True
            self.set_sprites(self.walk_left_animation)
        if self.x >= 0:
            walk_impulse = (-Player.RUNNING_FORCE, 0)
            center = (self.width // 2, self.height // 2)
            self.rb.apply_impulse_at_local_point(walk_impulse, center)

    def jump(self, engine):
        jump_impulse = (0, -engine.space.gravity[1] * Player.JUMP_FORCE)
        center = (self.width // 2, self.height // 2)
        self.rb.apply_impulse_at_local_point(jump_impulse, center)

    def idle(self):

        # stop all horizontal motion
        self.rb._set_velocity((0.00, self.rb.velocity[1]))

        self.pressed = False
        self.set_sprites(self.stand)

    def on_fixed_update(self, frame, engine):

        if keyboard.is_pressed(self.lru[1]):
            self.walk_right(engine)
        elif keyboard.is_pressed(self.lru[0]):
            self.walk_left()
        elif keyboard.is_pressed(self.lru[2]):
            self.jump(engine)
        else:
            self.idle()
