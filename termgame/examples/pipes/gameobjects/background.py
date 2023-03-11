from termgame import Engine, Gameobject, Screen


class Background(Gameobject):

    GRID_COLOR = (125, 125, 125)

    def __init__(self, grid_width, grid_height, grid_thickness, cell_thickness):
        self.screen_width = (grid_width * cell_thickness) + ((grid_width + 1) * grid_thickness)
        self.screen_height = (grid_height * cell_thickness) + ((grid_height + 1) * grid_thickness)

        s = Screen(self.screen_width, self.screen_height)
        s = s.fill((0, 0, 0))

        # fil in grid
        for i in range(0, self.screen_width, grid_thickness):
            for j in range(0, self.screen_height):
                if i % cell_thickness == 0:
                    print(i)
                    s = s.set_px_color(Background.GRID_COLOR, i, j)

        # for i, j in zip(range(self.screen_width), range(self.screen_height)):
        #     if i % grid_width == 0 and j % grid_height == 0:
        #         s = s.set_px_color(Background.GRID_COLOR, i, j)

        sprites = [s]
        Gameobject.__init__(self, sprites=sprites, depth=-1, name="Background")
