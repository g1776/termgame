"""Settings for the project."""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class LogSettings:
    level: str = os.getenv("LOG_LEVEL", "INFO")
    file: str = os.getenv("LOG_FILE", "logs/game.log")


@dataclass(frozen=True)
class Settings:
    logSettings: LogSettings = LogSettings()
