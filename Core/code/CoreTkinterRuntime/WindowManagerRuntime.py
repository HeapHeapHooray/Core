from .TCLRuntimeWindow import TCLRuntimeWindow
from . import TCL_Runtime

windows_set = set()

def add_window(window : TCLRuntimeWindow):
    global windows_set
    windows_set.add(window)
    TCL_Runtime.update()
def del_window(window : TCLRuntimeWindow):
    global windows_set
    windows_set.discard(window)
    window.destroy()
def delete_all_windows():
    global windows_set
    windows = [window for window in windows_set]
    for window in windows:
        window.delete_window()
def get_windows_count() -> int:
    global windows_set
    return len(windows_set)
def update():
    if get_windows_count() == 0:
        TCL_Runtime.stop_tcl()
