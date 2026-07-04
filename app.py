import sys

from PySide6.QtWidgets import QApplication

from src.app import TeslaERP


def main():
    app = QApplication(sys.argv)

    window = TeslaERP()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()