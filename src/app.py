from PySide6.QtWidgets import QMainWindow

from src.ui.main_window import MainWindow
from src.ui.styles import APP_STYLE


class TeslaERP(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("TeslaERP Pro")

        self.resize(1600, 900)

        self.setStyleSheet(APP_STYLE)

        self.main = MainWindow()

        self.setCentralWidget(self.main)

        self.statusBar().showMessage("Ready")