"""
Description: The base game engine.
Author: Gregory Glatzer
Date: 10/22/2022
"""

from __future__ import annotations

import bisect  # For sorting gameobjects by depth.
import os
import time
from typing import Callable, List, Dict, Any

# for hiding the cursor
import cursor  # type: ignore

from ..graphics.screen import Screen
from .gameobject import Gameobject
from ..settings import Settings


class Engine:
    def __init__(self, width: int, height: int, gameobjects: List[Gameobject] = None):
        self.width = width
        self.height = height
        self.screen = Screen(self.width, self.height)
        self.state: Dict[Any, Any] = {}
        self.__gameobjects: List[Gameobject] = []
        if gameobjects is not None:
            for gameobject in gameobjects:
                self.add_gameobject(gameobject)

    def clear(self) -> None:
        """
        Clear the screen without any blinking.
        """
        print(f"\033[{self.height}A\033[2K", end="")
        self.screen.clear()

    def add_gameobject(self, gameobject: Gameobject) -> None:
        """
        Add a gameobject to the engine.
        """
        bisect.insort(self.__gameobjects, gameobject, key=lambda go: go.depth)

    def get_gameobjects(self, names: str | List[str] = "") -> List[Gameobject]:
        """
        Get all gameobjects with given name(s). Empty returns all gameobjects.
        """
        if not names:
            return self.gameobjects

        if isinstance(names, str):
            names = [names]
        return [go for go in self.gameobjects if go.name in names]

    @property
    def gameobjects(self) -> List[Gameobject]:
        return self.__gameobjects

    @property
    def frame(self) -> int:
        return self.__frame

    @property
    def elapsed_time(self) -> float:
        return time.time() - self.__starting_time

    def run(self) -> None:
        """
        Run the engine.
        """

        self._run(None)

    def _run(
        self,
        runtime_injection: Callable[[Any], None] | None,
    ) -> None:
        self.__frame: int = 0
        self.__starting_time: float = time.time()

        # clear the screen of anything before we start
        cursor.hide()
        os.system("cls")

        if Settings.runtime_settings.wait_for_start:
            _ = input(
                f"Press any key to start the game at {Settings.runtime_settings.fps} fps."
                f" Recommended font size is {Settings.render_settings.fontsize}pt..."
            )

        # initialize the gameobjects
        for gameobject in self.gameobjects:
            gameobject.on_start(self)

        # start game loop
        while True:

            if Settings.runtime_settings.headless:
                print(f"Frame: {self.__frame}")

            # call on_update for each gameobject, passing the current frame
            # and the engine (so the gameobjects can access the game state)
            go_in_call_order = sorted(self.gameobjects, key=lambda go: go.update_order)
            for gameobject in go_in_call_order:
                gameobject.on_update(self.__frame, self)

            # call the runtime injection function, if it exists
            if runtime_injection:
                runtime_injection(self)

            if not Settings.runtime_settings.headless:

                # after updating the gameobjects, redraw them
                for gameobject in self.gameobjects:

                    # we can't draw gameobjects that don't have any sprites
                    if gameobject.get_sprites() is None or len(gameobject.get_sprites()) == 0:
                        continue

                    self.screen.paint_screen(
                        gameobject.get_active_sprite(), gameobject.x, gameobject.y
                    )

                self.screen.render()

            time.sleep(1 / Settings.runtime_settings.fps)

            if not Settings.runtime_settings.headless:
                self.clear()

            # update internal counters
            self.__frame += 1
