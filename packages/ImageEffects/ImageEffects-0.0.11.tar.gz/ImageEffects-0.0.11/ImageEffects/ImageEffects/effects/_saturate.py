# imports
from PIL import Image, ImageEnhance


class _saturate:
    '''Static class'''
    @classmethod
    def renderimage(cls, image: str, scale: int = 0) -> Image.Image:
        im = Image.open(image)
        _converter = ImageEnhance.Color(im)
        im = _converter.enhance(cls.getScale(scale))
        return im

    @classmethod
    def getScale(cls, scale: int = 0) -> float:
        if not isinstance(scale, int) or scale < 0:
            scale = 0
        elif scale > 10:
            scale = 10

        return float(scale)
