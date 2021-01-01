import numpy
from PIL import Image as PIL_Image
from typing import Tuple,Union
import CorePath
from . import ImageUtils
from . import ImageLib

def create_from_numpy_array(numpy_array: numpy.array) -> "Image" :
    from .Image import Image
    data = PIL_Image.fromarray(numpy_array)
    data = data.convert("RGBA")
    array = numpy.array(data)
    return Image(pixel_array=array)
def create_from_url(url: str) -> "Image" :
    array = ImageLib.download_as_numpy_array(url)
    image = create_from_numpy_array(array)
    image.set_title(url)
    return image
def create_from_image(image: "Image") -> "Image" :
    from .Image import Image
    new_image = Image(pixel_array=image.to_numpy_array())
    new_image.set_title(image.get_title())
    return new_image
def create_from_file(path_to_file: Union[CorePath.PathNode,str]) -> "Image":
    path_to_file = CorePath.Path.create_from_os_path_or_path_node(path_to_file)
    pil_image = PIL_Image.open(path_to_file.get_os_path())
    pil_image = pil_image.convert("RGBA")
    image = ImageUtils.convert_pil_to_image(pil_image)
    path_node = path_to_file
    file_name = path_node.get_name()
    image.set_title(file_name)
    return image
