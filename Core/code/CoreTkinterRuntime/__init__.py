from . import TCL_Runtime
from .TCLRuntimeWindow import TCLRuntimeWindow
from . import WindowManagerRuntime
from .ImageWindow import ImageWindow
from .VLCWindow import VLCWindow

def create_image_window(title: str,numpy_image):
    window = ImageWindow(title,numpy_image)
    return window

def get_count():
    return WindowManagerRuntime.get_windows_count()
