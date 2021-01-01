import numpy
from typing import Tuple,Union
from . import ImageUtils
from . import ImageFactory

class Selection:
    def __init__(self,mask: numpy.array):
        self._mask = mask

    def to_image(self) -> "Image":
        pixel_array = numpy.zeros((self._mask.shape[0],self._mask.shape[1],4),
                                  dtype=numpy.uint8)
        pixel_array[self._mask] = [255,255,255,255]
        pixel_array[~self._mask] = [0,0,0,255]

        image = ImageFactory.create_from_numpy_array(pixel_array)
        return image

    def to_numpy_array(self) -> numpy.array:
        return numpy.copy(self._mask)
    
    def display(self):
        display = ImageUtils.display_image(self.to_image())
        return display

    def select(self,selection):
        mask = selection.to_numpy_array()
        and_mask = numpy.logical_and.reduce((mask,self._mask))

        return Selection(and_mask)

    def deselect(self,selection):
        mask = selection.to_numpy_array()
        and_mask = numpy.logical_and.reduce((~mask,self._mask))

        return Selection(and_mask)

    def add_to_selection(self,selection):
        mask = selection.to_numpy_array()
        or_mask = numpy.logical_or.reduce((mask,self._mask))

        return Selection(or_mask)

    def is_pixel_selected(self,x: int,y: int) -> bool:
        return self._mask[x,y]

    def set_pixel_selected(self,x: int,y: int,selected: bool):
        self._mask[x,y] = selected

    def inverted(self):
        return Selection(~self._mask)

    def count_selected_pixels(self) -> int:
        return numpy.count_nonzero(self._mask)

    def get_width(self) -> int:
        height,width = self._mask.shape
        return width

    def get_height(self) -> int:
        height,width = self._mask.shape
        return height

    def get_size(self) -> Tuple[int,int]:
        return (self.get_width(),self.get_height())
