"""Settings for the project."""

from dotenv import load_dotenv
from dataclasses import dataclass
import os

load_dotenv()


@dataclass(frozen=True)
class LogSettings:
    level: str = os.getenv("LOG_LEVEL", "INFO")
    file: str = os.getenv("LOG_FILE", "logs/game.log")


@dataclass(frozen=True)
class Settings:
    logSettings: LogSettings = LogSettings()
