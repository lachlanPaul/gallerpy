"""
    All the instances, variables, functions, etc. That need to be accessed in more than one place.

    Lachlan Paul, 2024
"""
import os
from configparser import ConfigParser

from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget

# Config Paths
DATA_DIR = os.path.join(os.path.expanduser("~"), ".config", "gallerpy")
CONFIG_FILE = os.path.join(DATA_DIR, "config.ini")
DIRECTORY_FILE = os.path.join(DATA_DIR, "directory.json")

APP = QtWidgets.QApplication([])
CONFIG_PARSER = ConfigParser()

SCREEN_HEIGHT = APP.primaryScreen().size().height()
SCREEN_WIDTH = APP.primaryScreen().size().width()


def center_window(window: QWidget):
    """
        Does what it says on the tin. Centers the given window.
        :param window: the window to center
    """
    screen = APP.primaryScreen().availableGeometry()
    x = (screen.width() - window.width()) / 2
    y = (screen.height() - window.height()) / 2
    window.move(int(x), int(y))
