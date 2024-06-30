"""
    All the instances, variables, etc. That need to be accessed in more than one place.

    Lachlan Paul, 2024
"""
from PySide6 import QtWidgets

APP = QtWidgets.QApplication([])
SCREEN_HEIGHT = APP.primaryScreen().size().height()
SCREEN_WIDTH = APP.primaryScreen().size().width()