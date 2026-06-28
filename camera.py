from dataclasses import dataclass
from typing import Optional


@dataclass
class Camera:
    ip: str
    name: str = "Unknown Camera"
    manufacturer: str = "Unknown"
    model: str = "Unknown"
    rtsp_url: Optional[str] = None
    onvif: bool = False
    username: str = ""
    password: str = ""

    def display_name(self) -> str:
        return f"{self.name} ({self.ip})"
