import tkinter as tk
from PIL import Image as PIL_Image
from PIL import ImageTk
import numpy

from . import WindowManagerRuntime
from . import TCLRuntimeWindow

class ImageWindow(TCLRuntimeWindow):
        def __init__(self, title: str, numpy_image: numpy.array):

            self.image = PIL_Image.fromarray(numpy_image)
            width, height = self.image.size

            super().__init__(title,width,height)

            self.fullscreen = False
            self.window.bind("<F11>", self.toggle_fullscreen)
            self.window.bind("<Escape>", self.end_fullscreen)
            
            self.tk_image = ImageTk.PhotoImage(image=self.image)
            
            self.label = tk.Label(self.window, image=self.tk_image, width=width, height=height)
            self.label.pack(fill="both", expand="yes")
            self.label.bind("<Configure>", self.on_resize)

            self.window.lift()
            self.window.attributes("-topmost", True)
            self.window.after_idle(self.window.attributes, '-topmost', False)

            WindowManagerRuntime.add_window(self)

        def on_resize(self, event):
            self.width = event.width
            self.height = event.height
            self.update_image()

        def set_image(self,numpy_image : numpy.array):
            self.image = PIL_Image.fromarray(numpy_image)
            self.update_image()
            
        def update_image(self):
            width, height = self.image.size
            ratio = min(self.width / width, self.height / height)
            new_width = int(width * ratio)
            new_height = int(height * ratio)
            new_image = self.image.resize((new_width, new_height))
            self.tk_image = ImageTk.PhotoImage(image=new_image)
            if not self.destroyed:
                    self.label.configure(image=self.tk_image)

        def delete_window(self):
            self.on_delete()

        def on_delete(self):
            WindowManagerRuntime.del_window(self)

        def destroy(self):
            self.destroyed = True
            self.label.destroy()
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
