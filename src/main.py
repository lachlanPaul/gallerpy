"""
    The place where everything is called.

    Lachlan Paul, 2024
"""
import json
import os.path
import shutil

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QGridLayout, QWidget, QScrollArea, QComboBox, QMenuBar, QVBoxLayout

from src.components.image import *
from src.globals import APP, CONFIG_FILE, DIRECTORY_FILE, DATA_DIR, CONFIG_PARSER
from src.windows.directory_manager import DirectoryManagerWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()              # The main layout that manages every item in the window.
        self.menu_bar = QMenuBar()               # The menu bar.
        self.image_size_drop_down = QComboBox()  # A drop-down menu to.
        self.image_grid = QGridLayout()          # The grid that holds all the images.
        self.image_grid_widget = QWidget()       # The widget representation of said grid.
        self.grid_scroll = QScrollArea()         # The scroll area for the image grid.
        self.central_widget = QWidget()          # Everything. Has the main layout in it.

        # TODO: Make theme automatic and changeable in config.
        #   For some reason I couldn't get pyqtdarktheme to work,
        #   might have to look into fixing it or finding alternative.
        APP.setStyle("Fusion")

        # These variables are for placing items on the grid, and expanding or shrinking it when the window is resized.
        self.max_columns = 3
        self.current_row = 0
        self.current_column = 0

        self.setWindowTitle("gallery_py")

        # For some reason, this makes it so you can resize all the time.
        self.setMinimumSize(100, 100)

        self.load_data()
        self.setup_ui()
        self.get_images()

        self.showMaximized()

    def open_directory_manager(self):
        self.dir_manager_window = DirectoryManagerWindow()
        self.dir_manager_window.show()

    def add_to_grid(self, widget):
        self.image_grid.addWidget(widget, self.current_row, self.current_column)
        self.current_column += 1

        if self.current_column >= self.max_columns:
            self.current_column = 0
            self.current_row += 1

    def clear_grid(self):
        for i in reversed(range(self.image_grid.count())):
            widget = self.image_grid.itemAt(i).widget()
            self.image_grid.removeWidget(widget)
            widget.setParent(None)

    def get_images(self):
        # self.draw_images(path)
        pass

    def draw_images(self, path):
        for i in os.listdir(path):
            self.add_to_grid(ImageButton(Image(os.path.join(path, i))))

    def load_data(self):
        """
            Loads config data.
        """
        if not os.path.exists(DATA_DIR):
            os.mkdir(DATA_DIR)
        if not os.path.exists(CONFIG_FILE):
            shutil.copy("config.ini", CONFIG_FILE)
        if not os.path.exists(DIRECTORY_FILE):
            with open(DIRECTORY_FILE, "w") as file:
                json.dump({}, file)

        CONFIG_PARSER.read(CONFIG_FILE)

    def setup_ui(self):
        file_menu = self.menu_bar.addMenu("File")
        add_dir_action = QAction("Add Directory", self)

        # TODO: Find a better way then to have individual methods for each window, probably easy but I'm tired
        add_dir_action.triggered.connect(self.open_directory_manager)

        file_menu.addAction(add_dir_action)
        self.setMenuBar(self.menu_bar)

        # TODO: Add functionality
        # I don't know why it has to be like this.
        self.image_size_drop_down.setMaximumSize(50, self.image_size_drop_down.maximumSize().height())
        self.image_size_drop_down.addItems(["1", "2", "3", "4", "5", "6"])

        # Puts the grid into a widget, so we can put it in the layout
        self.image_grid_widget.setLayout(self.image_grid)

        self.grid_scroll.setWidgetResizable(True)
        self.grid_scroll.setWidget(self.image_grid_widget)

        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.layout.addWidget(self.image_size_drop_down)
        self.layout.addWidget(self.grid_scroll)


if __name__ == "__main__":
    window = MainWindow()
    window.show()
    APP.exec()
