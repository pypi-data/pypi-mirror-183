# imports
from PIL import Image, ImageOps


class _flip:
    '''Static class'''
    @staticmethod
    def renderimage(image: str) -> Image.Image:
        im = Image.open(image)
        im = ImageOps.flip(im)
        return im
