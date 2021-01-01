from PIL import ImageDraw as PIL_ImageDraw
from PIL import ImageFont
from . import ImageUtils

class ImageDraw:
    def __init__(self,image):
        self._size = image.get_size()
        self._image = ImageUtils.convert_image_to_pil(image)
        self._draw = PIL_ImageDraw.Draw(self._image)
        self._display = ImageUtils.create_image_display(image)
        self._title = image.get_title()

    def get_image(self):
        image = ImageUtils.convert_pil_to_image(self._image)
        image.set_title(self._title)
        return image

    def draw_update(func):
        def wrapper_draw_update(self,*args,**kwargs):
            func(self,*args,**kwargs)
            if not self._display.is_closed():
                self._display.set_image(self.get_image())
        return wrapper_draw_update

    def dynamic_display(self):
        self._display.set_image(self.get_image())
        self._display.open()

    def display(self):
        return self.get_image().display()
    
    @draw_update
    def draw_line(self,start_x,start_y,end_x,end_y,r,g,b):
        self._draw.line((start_x,start_y,end_x,end_y),fill=(r,g,b,255))

    @draw_update
    def draw_text(self,x,y,r,g,b,a,text,font_size=12):
        font = ImageFont.truetype("arial.ttf",font_size)
        self._draw.text((x,y),text,fill=(r,g,b,a),font=font)
