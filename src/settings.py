"""Settings for the project."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


def _bool(s: str) -> bool:
    return s.lower() in ("yes", "true", "t", "1")


@dataclass
class LogSettings:
    level: str = os.getenv("LOG_LEVEL", "INFO")
    file: str = os.getenv("LOG_FILE", "logs/game.log")


class RenderSettings:

    # The recommended font size for the terminal.
    # This will be recommended to the user before the game starts
    # if Settings.runtime_settings.wait_for_start is True (default).
    fontsize: int = int(os.getenv("FONT_SIZE", "6"))


class RuntimeSettings:

    # The number of frames per second to render
    fps: int = int(os.getenv("FPS", "20"))

    # Whether to run the game in headless mode
    headless: bool = _bool(os.getenv("HEADLESS", "False"))

    # The number of physics steps per frame
    ppf: int = int(os.getenv("PPF", "10"))

    # Whether to wait for the user to press a key before starting the game
    wait_for_start: bool = _bool(os.getenv("WAIT_FOR_START", "True"))


@dataclass(frozen=True)
class Settings:
    log_settings: LogSettings = LogSettings()
    render_settings: RenderSettings = RenderSettings()
    runtime_settings: RuntimeSettings = RuntimeSettings()
