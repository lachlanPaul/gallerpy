"""
    Window used to manage the directories to be scanned for images

    Lachlan Paul, 2024
"""
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QVBoxLayout, QFileDialog
from src.components.config_management import add_dir


class DirectoryManagerWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Directory Management")
        self.layout = QVBoxLayout()

        self.dir_list = QListWidget()
        self.add_button = QPushButton()
        self.remove_button = QPushButton()

        self.setup_ui()

    def setup_ui(self):
        self.add_button.clicked.connect(self.add_dir)

        self.layout.addWidget(self.dir_list)
        self.layout.addWidget(self.add_button)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def add_dir(self):
        dir_select = QFileDialog()
        dir_select.setFileMode(QFileDialog.FileMode.Directory)
        dir_to_add = dir_select.getExistingDirectory(self, "Add Directory")
        add_dir(dir_to_add, False)

