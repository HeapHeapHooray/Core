import platform
from .SystemInfo import SystemInfo

def get_system_info():
    return SystemInfo(platform.system())
