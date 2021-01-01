import tkinter as tk
import CoreSystem

from . import WindowManagerRuntime
from . import TCLRuntimeWindow

class VLCWindow(TCLRuntimeWindow):
        def __init__(self, title: str,player):
            self.player = player
            width, height = self.player.video_get_size()
            if width == 0 or height == 0:
                    width,height = 1280,720


            super().__init__(title,width,height)

            self.fullscreen = False
            self.window.bind("<F11>", self.toggle_fullscreen)
            self.window.bind("<Escape>", self.end_fullscreen)
            
            self.frame = tk.Frame(self.window, width=width, height=height)
            self.frame.pack(fill="both", expand="yes")

            system_info = CoreSystem.System.get_system_info()

            if system_info.is_windows():
                    self.player.set_hwnd(self.frame.winfo_id())
            elif system_info.is_linux():
                    self.player.set_xwindow(self.frame.winfo_id())
            
            self.window.lift()
            self.window.attributes("-topmost", True)
            self.window.after_idle(self.window.attributes, '-topmost', False)

            WindowManagerRuntime.add_window(self)
            
            self.player.play()

        def delete_window(self):
            self.on_delete()

        def on_delete(self):
            WindowManagerRuntime.del_window(self)
            self.player.stop()

        def destroy(self):
            self.destroyed = True
            self.window.destroy()

        def toggle_fullscreen(self, event=None):
            self.fullscreen = not self.fullscreen
            if not self.destroyed:
                    self.window.attributes("-fullscreen", self.fullscreen)

        def set_fullscreen(self, event=None):
            self.fullscreen = True
            if not self.destroyed:
                    self.window.attributes("-fullscreen", self.fullscreen)
                    
        def end_fullscreen(self, event=None):
            self.fullscreen = False
            if not self.destroyed:
                    self.window.attributes("-fullscreen", self.fullscreen)
                    
        def set_title(self,title : str):
            if not self.destroyed:
                    self.window.title(title)
        
        def is_destroyed(self):
                return self.destroyed
