"""
    The place where everything is called.

    Lachlan Paul, 2024
"""
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QGridLayout, QWidget, QScrollArea, QComboBox, QMenuBar, QVBoxLayout

from src.components.image import *
from src.globals import APP
from src.windows.directory_manager import DirectoryManagerWindow


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

        self.layout = QVBoxLayout()

        self.menu_bar = QMenuBar()
        file_menu = self.menu_bar.addMenu("File")
        add_dir_action = QAction("Add Directory", self)

        # TODO: Find a better way then to have individual methods for each window, probably easy but I'm tired
        add_dir_action.triggered.connect(self.open_directory_manager)

        file_menu.addAction(add_dir_action)
        self.setMenuBar(self.menu_bar)

        # TODO: Add functionality, maybe turn into toolbar?
        # This is the drop-down menu with options to change the image button sizes.
        self.image_size_drop_down = QComboBox()  # Sounds like something you'd order at KFC tbh.

        # I don't know why it has to be like this.
        self.image_size_drop_down.setMaximumSize(50, self.image_size_drop_down.maximumSize().height())
        self.image_size_drop_down.addItems(["1", "2", "3", "4", "5", "6"])

        # The grid that holds all the images.
        # Changes width based upon the window size, as well as user set image sizes.
        self.image_grid = QGridLayout()
        # self.image_grid.setColumnStretch(0, 50000)

        # Puts the grid into a widget, so we can put it in the layout
        self.image_grid_widget = QWidget()
        self.image_grid_widget.setLayout(self.image_grid)

        # Test, will remove. Ugly as, but has to be here until I add directory features
        self.add_to_grid(ImageButton(Image("as.png")))
        self.add_to_grid(ImageButton(Image("as.png")))
        self.add_to_grid(ImageButton(Image("as.png")))
        self.add_to_grid(ImageButton(Image("as.png")))
        self.add_to_grid(ImageButton(Image("as.png")))
        self.add_to_grid(ImageButton(Image("ha.png")))
        self.add_to_grid(ImageButton(Image("ha.png")))
        self.add_to_grid(ImageButton(Image("img_1.png")))

        # This is the scroll menu that the image grid will preside in.
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.image_grid_widget)

        # The central widget is literally everything.
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.layout.addWidget(self.image_size_drop_down)
        self.layout.addWidget(self.scroll_area)

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
        pass

    def draw_images(self):
        pass


if __name__ == "__main__":
    window = MainWindow()
    window.show()
    APP.exec()
