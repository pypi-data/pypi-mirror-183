# imports
from PIL import Image, ImageDraw
from numpy import dstack, array


class _cropcircle:
    '''Static class'''
    @staticmethod
    def renderimage(image: str) -> Image.Image:
        im = Image.open(image)
        _height, _width = im.size
        _lum_img = Image.new('L', (_height, _width), 0)

        draw = ImageDraw.Draw(_lum_img)
        draw.pieslice(((0, 0), (_height, _width)), 0, 360, fill=255, outline="white")

        _img_arr = array(im)
        _lum_img_arr = array(_lum_img)

        _final_img_arr = dstack((_img_arr, _lum_img_arr))
        im = Image.fromarray(_final_img_arr)
        return im
