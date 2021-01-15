import tkinter as tk
import CoreFileSystem
import CoreSystem

from . import TCL_Runtime

class TCLRuntimeWindow:
    def __init__(self,title: str,width: int,height: int):
        TCL_Runtime.set_running()
        self.destroyed = False
        self.window = tk.Toplevel(width=width, height=height)
        self.width = width
        self.height = height

        self.window.protocol("WM_DELETE_WINDOW", self.on_delete)

        self.window.title(title)

        system_info = CoreSystem.System.get_system_info()

        core_directories = CoreFileSystem.CoreDirectories
        assets_folder = core_directories.get_assets_directory_path()
        icon_name = "Blank-256.ico"
        if system_info.is_linux():
                icon_name = "Blank-256.xbm"
        icon = assets_folder.create_node(icon_name)
        if system_info.is_windows():
                self.window.iconbitmap(default=icon.get_os_path())
        else:
                self.window.iconbitmap("@"+icon.get_os_path())
