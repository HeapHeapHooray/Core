import numpy
from PIL import Image as PIL_Image
from typing import Tuple,Union
import CorePath
from .Pixel import Pixel
from . import ImageUtils
from . import ImageLib
from . import ImageFactory
from . import ImageOperations
from .Selection import Selection

class Image:
    def __init__(self,width: int = 0,height: int = 0,pixel_array: numpy.array = None,title: str = "Untitled"):
        width = max(width,1)
        height = max(height,1)
        if not pixel_array is None:
            self.__pixel_array = numpy.copy(pixel_array)
        else:
            self.__pixel_array = numpy.zeros((width,height,4),dtype=numpy.uint8)
        self.title = str(title)
    def set_title(self,title: str):
        self.title = str(title)
    def get_title(self) -> str:
        return str(self.title)
    def display(self):
        return ImageUtils.display_image(self)
    def cropped(self,start_x: int,start_y: int,end_x: int,end_y: int):
        cropped_array = numpy.copy(self.__pixel_array)
        cropped_array = cropped_array[start_y:end_y,start_x:end_x]
        return ImageFactory.create_from_numpy_array(cropped_array)
    def resized(self,new_width: int,new_height: int):
        return ImageOperations.resize_nearest(self,new_width,new_height)
    def rotated(self,angle: float):
        return ImageOperations.rotate(self,angle)
    def clone(self):
        return ImageFactory.create_from_image(self)
    def set_pixel_array(self,pixel_array):
        self.__pixel_array = numpy.copy(pixel_array)
    def iterpixels(self):
        current_pixel = Pixel(0,0,0,0)
        image_data = PIL_Image.fromarray(self.to_numpy_array()).getdata()
        width,height = self.get_size()
        for x in range(width):
            for y in range(height):
                current_pixel.set_rgba(*(image_data[y * width + x]))
                yield current_pixel
                self.set_pixel(x, y, current_pixel)
    def get_pixel(self,x: int,y: int) -> Pixel :
        r,g,b,a = self.__pixel_array[y,x]
        return Pixel(r,g,b,a)
    def set_pixel(self,x: int,y: int,pixel: Pixel):
        self.__pixel_array[y,x] = pixel.get_rgba()
    def set_pixel_rgba(self,x: int,y: int,r: int,g: int,b: int,a: int):
        self.__pixel_array[y,x] = r,g,b,a
    def get_width(self) -> int :
        height,width,_ = self.__pixel_array.shape
        return width
    def get_height(self) -> int :
        height,width,_ = self.__pixel_array.shape
        return height
    def get_size(self) -> Tuple[int,int] :
        return (self.get_width(),self.get_height())
    def get_pixels_count(self) -> int:
        return self.get_width()*self.get_height()
    def to_numpy_array(self) -> numpy.array:
        return numpy.copy(self.__pixel_array)
    def equals(self,image) -> bool :
        return numpy.array_equal(self.to_numpy_array(),image.to_numpy_array())
    def select_greater_than(self,r: int = None,g: int = None,b: int = None
                           ,a: int = None):
        comparisons = []
        if not r is None:
            comparisons.append(self.__pixel_array[:,:,0] > r)
        if not g is None:
            comparisons.append(self.__pixel_array[:,:,1] > g)
        if not b is None:
            comparisons.append(self.__pixel_array[:,:,2] > b)
        if not a is None:
            comparisons.append(self.__pixel_array[:,:,3] > a)

        if len(comparisons) < 1:
            return self.select_all()

        mask = numpy.logical_and.reduce(comparisons)
        return Selection(mask)

    def select_lesser_than(self,r: int = None,g: int = None,b: int = None
                           ,a: int = None):
        comparisons = []
        if not r is None:
            comparisons.append(self.__pixel_array[:,:,0] < r)
        if not g is None:
            comparisons.append(self.__pixel_array[:,:,1] < g)
        if not b is None:
            comparisons.append(self.__pixel_array[:,:,2] < b)
        if not a is None:
            comparisons.append(self.__pixel_array[:,:,3] < a)

        if len(comparisons) < 1:
            return self.select_all()

        mask = numpy.logical_and.reduce(comparisons)
        return Selection(mask)

    def select_equal_to(self,r: int = None,g: int = None,b: int = None
                           ,a: int = None):
        comparisons = []
        if not r is None:
            comparisons.append(self.__pixel_array[:,:,0] == r)
        if not g is None:
            comparisons.append(self.__pixel_array[:,:,1] == g)
        if not b is None:
            comparisons.append(self.__pixel_array[:,:,2] == b)
        if not a is None:
            comparisons.append(self.__pixel_array[:,:,3] == a)

        if len(comparisons) < 1:
            return self.select_all()
        
        mask = numpy.logical_and.reduce(comparisons)
        return Selection(mask)

    def select_all(self):
        mask = numpy.ones((self.get_height(),self.get_width()),
                          dtype=numpy.bool_)

        return Selection(mask)

    def flipped_horizontally(self):
        return ImageOperations.flip_horizontally(self)

    def flipped_vertically(self):
        return ImageOperations.flip_vertically(self)

    def save_to_file(self,path_to_file: Union[CorePath.PathNode,str]):
        path_to_file = CorePath.Path.create_from_os_path_or_path_node(path_to_file)
        ImageLib.save_to_file(self,path_to_file.get_os_path())

    def os_display(self):
        ImageUtils.os_display_image(self)
