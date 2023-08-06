# imports
from PIL import Image, ImageOps


class _mirror:
    '''Static class'''
    @staticmethod
    def renderimage(image: str) -> Image.Image:
        im = Image.open(image)
        im = ImageOps.mirror(im)
        return im
