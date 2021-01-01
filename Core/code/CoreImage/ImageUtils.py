import numpy
from PIL import Image as PIL_Image


def create_image_display(image: "Image" ):
    from .Image import Image
    import CoreGUI
    if image is None:
        image = Image(1,1)
    display = CoreGUI.ImageDisplay(image)
    return display
def display_image(image: "Image"):
    display = create_image_display(image)
    display.open()
    return display
def os_display_image(image: "Image"):
    pil_image = convert_image_to_pil(image)
    pil_image.show()
def convert_image_to_pil(image: "Image") -> PIL_Image:
    array = image.to_numpy_array()
    pil_image = PIL_Image.fromarray(array)
    return pil_image
def convert_pil_to_image(pil: PIL_Image) -> "Image":
    from . import ImageFactory
    pil = pil.convert("RGBA")
    array = numpy.array(pil)
    return ImageFactory.create_from_numpy_array(array)
