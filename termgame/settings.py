"""Settings for the project."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv


def _bool(s: str) -> bool:
    """
    Convert a string to a boolean.

    Args:
        s (str): The string to convert.

    Returns:
        bool: The boolean value of the string.

    """
    return s.lower() in ("yes", "true", "t", "1")


@dataclass
class LogSettings:
    """
    A class for configuring logging settings.

    Attributes:
        level (str): The logging level (default: "INFO").
        file (str): The file to log to (default: "logs/game.log").

    """

    level: str = os.getenv("LOG_LEVEL", "INFO")
    file: str = os.getenv("LOG_FILE", "logs/game.log")


class RenderSettings:
    """
    A class for configuring rendering settings.

    Attributes:
        fontsize (int): The recommended font size for the terminal
            (default: 6).

    """

    fontsize: int = int(os.getenv("FONT_SIZE", "6"))


class RuntimeSettings:
    """
    A class for configuring runtime settings.

    Attributes:
        fps (int): The number of frames per second to render
            (default: 20).
        headless (bool): Whether to run the game in headless mode
            (default: False).
        ppf (int): The number of physics steps per frame
            (default: 10).
        wait_for_start (bool): Whether to wait for the user to press a
            key before starting the game (default: True).

    """

    fps: int = int(os.getenv("FPS", "20"))
    headless: bool = _bool(os.getenv("HEADLESS", "False"))
    ppf: int = int(os.getenv("PPF", "10"))
    wait_for_start: bool = _bool(os.getenv("WAIT_FOR_START", "True"))


@dataclass(frozen=True)
class Settings:
    """
    A class for configuring all settings required for the project.

    Attributes:
        log_settings (LogSettings): An instance of LogSettings.
        render_settings (RenderSettings): An instance of RenderSettings.
        runtime_settings (RuntimeSettings): An instance of RuntimeSettings.

    """

    log_settings: LogSettings = LogSettings()
    render_settings: RenderSettings = RenderSettings()
    runtime_settings: RuntimeSettings = RuntimeSettings()
