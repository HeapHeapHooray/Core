import CoreTkinterRuntime
import CoreImage

class ImageDisplay:
    def __init__(self,image: CoreImage.Image , title: str = None):
        self.title = title
        self._image_window = None
        if self.title is None:
            self.title = image.get_title()
        self.image = image
    def set_title(self,title: str):
        self.title = title
        self.update()
    def set_image(self,image: CoreImage.Image,set_title: bool = True):
        self.image = image.clone()
        if set_title:
            self.title = image.get_title()
        self.update()
    def get_image(self) -> CoreImage.Image :
        return self.image.clone()
    def get_title(self) -> str :
        return str(self.title)
    def set_fullscreen(self,fullscreen: bool):
        if fullscreen == True:
            self._image_window.set_fullscreen()
        else:
            self._image_window.end_fullscreen()
    def open(self):
        if self.is_closed():
            numpy_image = self.image.to_numpy_array()
            self._image_window = CoreTkinterRuntime.create_image_window(self.title,numpy_image)
        self.update()
    def close(self):
        if not self.is_closed():
            self._image_window.delete_window()
    def is_closed(self) -> bool :
        return self._image_window is None or self._image_window.is_destroyed()
    def update(self):
        if not self.is_closed():
            self._image_window.set_title(self.title)
            self._image_window.set_image(self.image.to_numpy_array())
