import sys
from PySide6.QtWidgets import QApplication
from gui import CameraManagerWindow


def main():
    app = QApplication(sys.argv)
    window = CameraManagerWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
