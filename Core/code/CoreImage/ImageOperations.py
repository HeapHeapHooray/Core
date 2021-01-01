import numpy
from PIL import Image as PIL_Image
from . import ImageUtils

def pil_resize(image: "Image",new_width: int,new_height: int,method=PIL_Image.NEAREST) -> "Image" :
    pil_image = ImageUtils.convert_image_to_pil(image)
    pil = pil_image.resize((new_width,new_height),method)
    array = numpy.array(pil)
    output_image = image.clone()
    output_image.set_pixel_array(array)
    return output_image
def resize_nearest(image: "Image",new_width: int,new_height: int) -> "Image" :
    return pil_resize(image,new_width,new_height,PIL_Image.NEAREST)
def pil_rotate(image: "Image",angle: float) -> "Image" :
    pil_image = ImageUtils.convert_image_to_pil(image)
    pil =  pil_image.rotate(angle)
    array = numpy.array(pil)
    output_image = image.clone()
    output_image.set_pixel_array(array)
    return output_image
def rotate(image: "Image",angle: float) -> "Image" :
    return pil_rotate(image,angle)
def pil_transpose(image: "Image",method=PIL_Image.TRANSPOSE) -> "Image":
    pil_image = ImageUtils.convert_image_to_pil(image)
    transposed = pil_image.transpose(method)
    output_image = ImageUtils.convert_pil_to_image(transposed)
    return output_image
def flip_horizontally(image: "Image") -> "Image":
    return pil_transpose(image,PIL_Image.FLIP_LEFT_RIGHT)
def flip_vertically(image: "Image") -> "Image":
    return pil_transpose(image,PIL_Image.FLIP_TOP_BOTTOM)
