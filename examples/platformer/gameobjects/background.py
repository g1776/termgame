from termgame import *
from termgame.util import scroll_sprite
import os


class Background(Gameobject):
    SPRITES_FOLDER = os.path.dirname(os.path.abspath(__file__)) + "/../sprites/"

    def __init__(self, screen_width, screen_height):
        sprites = [
            Screen.from_image(
                Background.SPRITES_FOLDER + "background.png", (screen_width, screen_height)
            )
        ]
        Gameobject.__init__(
            self, sprites=sprites, depth=-1, on_update=self.on_update, name="Background"
        )

    def on_update(self, frame, engine: Engine):

        # scroll the background every 10 frammes
        if frame % 10 == 0:
            self.sprites[0] = scroll_sprite(self.sprites[0], -1, 0)
