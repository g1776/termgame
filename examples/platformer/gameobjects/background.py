import os

from termgame import *
from termgame.util import scroll_sprite


class Background(Gameobject):
    SPRITES_FOLDER = os.path.dirname(os.path.abspath(__file__)) + "/../sprites/"

    def __init__(self, screen_width, screen_height):
        self.background_image = Screen.from_image(
            Background.SPRITES_FOLDER + "background.png",
            (screen_width, screen_height),
        )
        sprites = [self.background_image]
        Gameobject.__init__(
            self, sprites=sprites, depth=-1, on_update=self.on_update, name="Background"
        )

    def on_update(self, frame, engine: Engine):

        # scroll the background every 10 frammes
        if frame % 10 == 0:
            self.background_image = scroll_sprite(self.background_image, -1, 0)
            self.set_sprites([self.background_image])
