"""
logger.py
Description: Logging for the application
Author: Gregory Glatzer
Date: 12/12/2022
"""

import logging
import os

from .settings import Settings

# create logger
Logger = logging.getLogger("game")
Logger.setLevel(Settings.log_settings.level)

formatter = logging.Formatter("%(filename)s:%(lineno)s - %(message)s")

# # create console handler and add formatting
# sh = logging.StreamHandler()
# sh.setFormatter(formatter)
# # add ch to logger
# Logger.addHandler(sh)

# add logging file

# create the logging file and subfolders if they don't exist
if not os.path.exists(os.path.dirname(Settings.log_settings.file)):
    os.makedirs(os.path.dirname(Settings.log_settings.file))


fh = logging.FileHandler(Settings.log_settings.file)
fh.setFormatter(formatter)
Logger.addHandler(fh)
