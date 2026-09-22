import sys

from PySide6.QtWidgets import QApplication

from ui.desktop import IrisWindow


def main():

    app = QApplication(sys.argv)

    window = IrisWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()