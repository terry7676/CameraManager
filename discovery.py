import ipaddress
import socket
from camera import Camera

COMMON_PORTS = [80, 554, 8000, 8080]


def is_host_alive(ip: str, timeout: float = 0.2):
    for port in COMMON_PORTS:
        try:
            with socket.create_connection((ip, port), timeout=timeout):
                return True
        except OSError:
            pass
    return False


def discover_cameras(network: str = "192.168.1.0/24"):
    cameras = []

    for ip in ipaddress.IPv4Network(network, strict=False):
        ip_str = str(ip)
        if is_host_alive(ip_str):
            cameras.append(Camera(ip=ip_str, name="Network Device"))

    return cameras
