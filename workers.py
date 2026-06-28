from PySide6.QtCore import QThread, Signal
from discovery import discover_cameras


class DiscoveryWorker(QThread):
    cameras_found = Signal(list)

    def run(self):
        cameras = discover_cameras()
        self.cameras_found.emit(cameras)
