"""
    Window used to manage the directories to be scanned for images

    Lachlan Paul, 2024
"""
from PySide6.QtWidgets import QWidget


class DirectoryManagerWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Directory Management")
