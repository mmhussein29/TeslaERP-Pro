from PySide6.QtWidgets import *

from src.ui.sidebar import Sidebar
from src.ui.workspace import Workspace


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        self.sidebar = Sidebar()
        self.workspace = Workspace()

        layout.addWidget(self.sidebar)
        layout.addWidget(self.workspace)

        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)