from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QListWidget, QLabel, QFrame, QStatusBar
)
from PySide6.QtCore import Qt


class CameraManagerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Camera Manager')
        self.resize(1200, 700)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout(central)

        left = QVBoxLayout()

        self.scan_button = QPushButton('Discover Cameras')
        self.camera_list = QListWidget()

        left.addWidget(self.scan_button)
        left.addWidget(self.camera_list)

        self.preview = QLabel('Live Preview')
        self.preview.setAlignment(Qt.AlignCenter)
        self.preview.setFrameShape(QFrame.Box)

        layout.addLayout(left, 1)
        layout.addWidget(self.preview, 2)

        status = QStatusBar()
        status.showMessage('Ready')
        self.setStatusBar(status)
