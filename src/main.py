"""
    The place where everything is called.

    Lachlan Paul, 2024
"""
from PySide6 import QtWidgets
from PySide6.QtWidgets import QGridLayout, QWidget, QSizePolicy, QScrollArea

from src.components.image import *
from src.globals import APP, SCREEN_WIDTH


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # These variables are for placing items on the grid, and expanding or shrinking it when the window is resized.
        self.max_columns = 3
        self.current_row = 0
        self.current_column = 0

        self.setWindowTitle("gallery_py")

        # For some reason, this makes it so you can resize all the time.
        self.setMinimumSize(100, 100)

        self.imgs = []

        self.layout = QGridLayout()
        self.layout.setColumnStretch(0, 50000)

        # test, will remove
        self.add_to_grid(ImageButton(Image("gorgon.png")))
        self.add_to_grid(ImageButton(Image("gorgon.png")))
        self.add_to_grid(ImageButton(Image("gorgon.png")))
        self.add_to_grid(ImageButton(Image("gorgon.png")))
        self.add_to_grid(ImageButton(Image("gorgon.png")))
        self.add_to_grid(ImageButton(Image("capture.jpg")))

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        # Makes it so the app is scrollable
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(widget)
        self.setCentralWidget(self.scroll_area)

        self.showMaximized()

    def add_to_grid(self, widget):
        self.layout.addWidget(widget, self.current_row, self.current_column)
        self.imgs.append(widget)
        self.current_column += 1

        if self.current_column >= self.max_columns:
            self.current_column = 0
            self.current_row += 1

    def clear_grid(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            self.layout.removeWidget(widget)
            widget.setParent(None)

    def get_images(self):
        pass

    def draw_images(self):
        pass


if __name__ == "__main__":
    window = MainWindow()
    window.show()
    APP.exec()
