import numpy
from skimage import io
from typing import Tuple,Union
import CorePath
from . import ImageUtils

def skimage_download_as_numpy_array(url: str) -> numpy.array :
    return io.imread(url)
def download_as_numpy_array(url: str) -> numpy.array :
    return skimage_download_as_numpy_array(url)
def save_to_file(image: "Image",path_to_file: Union[CorePath.PathNode,str]):
    path_to_file = CorePath.Path.create_from_os_path_or_path_node(path_to_file)
    pil_image = ImageUtils.convert_image_to_pil(image)
    pil_image.save(path_to_file.get_os_path(),"PNG")
