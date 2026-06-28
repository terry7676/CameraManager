from PySide6.QtWidgets import QMainWindow,QWidget,QHBoxLayout,QVBoxLayout,QPushButton,QListWidget,QLabel,QFrame,QStatusBar
from PySide6.QtCore import Qt
from workers import DiscoveryWorker

class CameraManagerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Camera Manager')
        self.resize(1200,700)
        central=QWidget(); self.setCentralWidget(central)
        layout=QHBoxLayout(central)
        left=QVBoxLayout()
        self.scan_button=QPushButton('Discover Cameras')
        self.camera_list=QListWidget()
        left.addWidget(self.scan_button); left.addWidget(self.camera_list)
        self.preview=QLabel('Live Preview')
        self.preview.setAlignment(Qt.AlignCenter)
        self.preview.setFrameShape(QFrame.Box)
        layout.addLayout(left,1); layout.addWidget(self.preview,2)
        self.status=QStatusBar(); self.setStatusBar(self.status)
        self.status.showMessage('Ready')
        self.scan_button.clicked.connect(self.start_scan)
    def start_scan(self):
        self.status.showMessage('Scanning network...')
        self.scan_button.setEnabled(False)
        self.worker=DiscoveryWorker()
        self.worker.cameras_found.connect(self.populate)
        self.worker.finished.connect(lambda: self.scan_button.setEnabled(True))
        self.worker.start()
    def populate(self,cameras):
        self.camera_list.clear()
        for cam in cameras:
            self.camera_list.addItem(cam.display_name())
        self.status.showMessage(f'Found {len(cameras)} device(s)')