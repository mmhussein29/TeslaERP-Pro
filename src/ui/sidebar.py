from PySide6.QtWidgets import *
from PySide6.QtCore import Qt


class Sidebar(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("Sidebar")
        self.setFixedWidth(220)

        layout = QVBoxLayout()

        title = QLabel("TeslaERP Pro")
        title.setObjectName("Title")

        layout.addWidget(title)

        menu = [
            "Dashboard",
            "CRM",
            "Sales",
            "Purchasing",
            "Inventory",
            "Projects",
            "Accounting",
            "HR",
            "Reports",
            "Settings"
        ]

        for item in menu:
            btn = QPushButton(item)
            btn.setCursor(Qt.PointingHandCursor)
            layout.addWidget(btn)

        layout.addStretch()

        self.setLayout(layout)