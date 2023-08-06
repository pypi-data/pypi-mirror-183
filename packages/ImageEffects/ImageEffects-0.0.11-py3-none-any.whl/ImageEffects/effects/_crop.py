# imports
from PIL import Image


class _crop:
    '''Static class'''
    @classmethod
    def renderimage(cls, image: str) -> Image.Image:
        im = Image.open(image)
        im = im.crop(cls.getBoxCord(im))
        return im

    @classmethod
    def getBoxCord(cls, image: Image.Image) -> tuple:
        new_size = image.width if image.width < image.height else image.height
        left = int(image.width/2) - int(new_size/2)
        upper = int(image.height/2) - int(new_size/2)
        right = int(image.width/2) + int(new_size/2)
        lower = int(image.height/2) + int(new_size/2)

        _cord = (left, upper, right, lower)
        return _cord
