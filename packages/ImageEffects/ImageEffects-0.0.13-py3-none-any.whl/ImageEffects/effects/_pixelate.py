# imports
from PIL import Image


class _pixelate:
    '''Static class'''
    PIXELATE_SIZES = [8, 16, 32, 64, 128, 256, 512]

    @classmethod
    def renderimage(cls, image: str, scale: int = 0) -> Image.Image:
        im = Image.open(image)
        imSmall = im.resize(cls.getPixelateSize(scale), resample=Image.Resampling.BILINEAR)
        im = imSmall.resize(im.size, Image.Resampling.NEAREST)
        return im

    @classmethod
    def getPixelateSize(cls, scale: int = 0):
        if not isinstance(scale, int) or scale < 0:
            scale = 0
        elif scale > 6:
            scale = 6

        return (cls.PIXELATE_SIZES[scale], cls.PIXELATE_SIZES[scale])
