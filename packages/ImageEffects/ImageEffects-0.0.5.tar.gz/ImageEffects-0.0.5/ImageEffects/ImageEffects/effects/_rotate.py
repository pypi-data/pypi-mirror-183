# imports
from PIL import Image


class _rotate:
    '''Static class'''
    @staticmethod
    def renderimage(image: str, rotation_angle: int = 1) -> Image.Image:
        im = Image.open(image).rotate(rotation_angle)
        return im
