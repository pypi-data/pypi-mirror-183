# imports
from PIL import Image, ImageEnhance


class _deepfry:
    '''Static class'''
    LOWER_RESOLUTION = (256, 256)
    SATURATION_ENHANCE_SCALE = 2.0
    RED_BAND_INCREASE_RATIO = 3.0
    BLUE_BAND_INCREASE_RATIO = 0.5
    CONTRAST_INCREASE_FACTOR = 3.0

    @classmethod
    def renderimage(cls, image: str) -> Image.Image:
        im = Image.open(image)

        # lowering resolution
        imSmall = im.resize(cls.LOWER_RESOLUTION, resample=Image.Resampling.BILINEAR)
        im = imSmall.resize(im.size, Image.Resampling.NEAREST)

        # increasing saturation
        _converter_saturation = ImageEnhance.Color(im)
        im = _converter_saturation.enhance(cls.SATURATION_ENHANCE_SCALE)

        # increasing red band's saturation
        # and decreasing blue band's saturation to increase yellow's
        r, g, b = im.split()
        r = r.point(lambda i: i * cls.RED_BAND_INCREASE_RATIO)
        b = b.point(lambda i: i * cls.BLUE_BAND_INCREASE_RATIO)
        im = Image.merge('RGB', (r, g, b))

        # increasing constrast
        _converter_contrast = ImageEnhance.Contrast(im)
        im = _converter_contrast.enhance(cls.CONTRAST_INCREASE_FACTOR)

        return im
