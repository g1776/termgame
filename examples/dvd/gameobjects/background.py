from termgame import Gameobject, Screen


class Background(Gameobject):
    def __init__(self, screen_width, screen_height):
        sprites = [Screen(screen_width, screen_height).fill((255, 255, 255))]
        Gameobject.__init__(self, sprites=sprites, depth=-1, name="Background")
