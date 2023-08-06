# imports
from PIL import Image


class _resize:
    '''Static class'''
    @classmethod
    def renderimage(cls, image: str, width: int = 100, height: int = 100) -> Image.Image:
        im = Image.open(image)
        im = im.resize(cls.getSize(im, width, height))
        return im

    @classmethod
    def getSize(cls, im: Image.Image, width: int, height: int) -> tuple:
        '''filters width and height input'''
        if not isinstance(width, int) or width > im.width or width < 1:
            width = im.width

        if not isinstance(height, int) or height > im.height or height < 1:
            height = im.height

        return (width, height)
