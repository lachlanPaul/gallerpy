"""
    Window to show individual image

    Lachlan Paul, 2024
"""
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget

from src.globals import SCREEN_WIDTH, SCREEN_HEIGHT, center_window


class ImageWindow(QWidget):
    """
        Window created to display an image
    """

    def __init__(self, image):
        super().__init__()

        self.setWindowTitle(image.path)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(image)

        self.setLayout(self.layout)
        self.resize(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 3))

        center_window(self)
        self.show()
