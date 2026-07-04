from PySide6.QtWidgets import *


class Workspace(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel("Welcome to TeslaERP Pro")

        label.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        layout.addWidget(label)

        self.setLayout(layout)