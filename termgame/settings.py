"""
Settings for the project.
"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv


def _bool(s: str) -> bool:
    """
    Convert a string to a boolean.

    :param s: The string to convert.
    :type s: str
    :return: The boolean value of the string.
    :rtype: bool
    """
    return s.lower() in ("yes", "true", "t", "1")


@dataclass
class LogSettings:
    """
    A class for configuring logging settings.

    :ivar level: The logging level (default: "INFO").
    :vartype level: str
    :ivar file: The file to log to (default: "logs/game.log").
    :vartype file: str
    """

    level: str = os.getenv("LOG_LEVEL", "INFO")
    file: str = os.getenv("LOG_FILE", "logs/game.log")


@dataclass
class RenderSettings:
    """
    A class for configuring rendering settings.

    :ivar fontsize: The recommended font size for the terminal (default: 6).
    :vartype fontsize: int
    """

    fontsize: int = int(os.getenv("FONT_SIZE", "6"))


@dataclass
class RuntimeSettings:
    """
    A class for configuring runtime settings.

    :ivar fps: The number of frames per second to render (default: 20).
    :vartype fps: int
    :ivar headless: Whether to run the game in headless mode (default: False).
    :vartype headless: bool
    :ivar ppf: The number of physics steps per frame (default: 10).
    :vartype ppf: int
    :ivar wait_for_start: Whether to wait for the user to press a key before starting the game (default: True).
    :vartype wait_for_start: bool
    """

    fps: int = int(os.getenv("FPS", "20"))
    headless: bool = _bool(os.getenv("HEADLESS", "False"))
    ppf: int = int(os.getenv("PPF", "10"))
    wait_for_start: bool = _bool(os.getenv("WAIT_FOR_START", "True"))


@dataclass(frozen=True)
class Settings:
    """
    A class for configuring all settings required for the project.

    :ivar log_settings: An instance of LogSettings.
    :vartype log_settings: LogSettings
    :ivar render_settings: An instance of RenderSettings.
    :vartype render_settings: RenderSettings
    :ivar runtime_settings: An instance of RuntimeSettings.
    :vartype runtime_settings: RuntimeSettings
    """

    log_settings: LogSettings = LogSettings()
    render_settings: RenderSettings = RenderSettings()
    runtime_settings: RuntimeSettings = RuntimeSettings()
