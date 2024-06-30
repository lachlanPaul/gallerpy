"""
    All classes related to images.

    Lachlan Paul, 2024
"""

from PySide6 import QtWidgets, QtGui, QtCore
from src.windows.image_window import ImageWindow


class Image(QtWidgets.QLabel):
    def __init__(self, image_path: str):
        """
            :param image_path: A string representing a path to a Qt readable image file.
        """
        super().__init__()
        pixmap = QtGui.QPixmap(image_path)
        self.path = image_path
        self.setPixmap(pixmap)


class ImageButton(QtWidgets.QPushButton):
    def __init__(self, image: Image):
        super().__init__()

        self.image = image

        pixmap = QtGui.QPixmap(image.pixmap())
        icon = QtGui.QIcon(pixmap)
        self.setIcon(icon)
        self.setIconSize(pixmap.rect().size())
        self.maximumHeight()
        self.setStyleSheet("border: none;")

        self.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

        self.clicked.connect(self.on_click)

    def on_click(self):
        # This is set to a class variable to stop it being garbage collected, which would remove it instantly
        self.image_window = ImageWindow(self.image)
