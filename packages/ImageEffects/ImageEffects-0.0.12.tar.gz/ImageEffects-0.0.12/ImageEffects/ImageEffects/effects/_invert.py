# imports
from PIL import Image, ImageOps


class _invert:
    '''Static class'''
    @staticmethod
    def renderimage(image: str) -> Image.Image:
        im = Image.open(image)
        im = ImageOps.invert(im)
        return im
