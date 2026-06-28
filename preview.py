import cv2
from PySide6.QtCore import QThread, Signal


class PreviewWorker(QThread):
    frame_ready = Signal(object)
    status_changed = Signal(str)

    def __init__(self, rtsp_url: str):
        super().__init__()
        self.rtsp_url = rtsp_url
        self._running = True

    def run(self):
        self.status_changed.emit(f"Connecting to {self.rtsp_url}...")
        cap = cv2.VideoCapture(self.rtsp_url)

        if not cap.isOpened():
            self.status_changed.emit("Unable to open RTSP stream")
            return

        self.status_changed.emit("Streaming")

        while self._running:
            ok, frame = cap.read()
            if not ok:
                break
            self.frame_ready.emit(frame)

        cap.release()
        self.status_changed.emit("Disconnected")

    def stop(self):
        self._running = False
        self.wait()
