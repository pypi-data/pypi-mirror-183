# imports
from PIL import Image
from PIL import ImageFilter


class _blur:
    '''Static class'''
    @staticmethod
    def renderimage(image: str, radius: int = 1) -> Image.Image:
        im = Image.open(image)
        im = im.filter(ImageFilter.BoxBlur(radius))
        return im
