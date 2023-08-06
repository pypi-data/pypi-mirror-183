# imports
from PIL import Image, ImageDraw, ImageFont
from importlib import resources
import io
from ImageEffects.utils import format_text


class _caption2:
    '''Static class'''
    TEXT_COLOR = (255, 255, 255)
    FONT_SIZE_RATIO = 7/100  # 7%
    LINE_LENGTH = int(FONT_SIZE_RATIO * 100 * 3)
    FONT_HEIGHT = FONT_SIZE_RATIO * 100 * 6

    @classmethod
    def renderimage(cls, image: str, text: str = 'text here', _font_size_ratio_mul: float = 1.0) -> Image.Image:
        if len(text) == 0:
            text = 'text here'

        text = format_text(cls.LINE_LENGTH, text)

        with resources.open_binary('resources.fonts', 'impact.ttf') as fp:
            _font_file = io.BytesIO(fp.read())

        im = Image.open(image)
        editable_im = ImageDraw.Draw(im)

        FONT = ImageFont.truetype(_font_file, int(cls.FONT_SIZE_RATIO * _font_size_ratio_mul * im.width))
        _, _, _w, _h = editable_im.textbbox((0, 0), text, font=FONT)

        editable_im.text(((im.width - _w)/2, im.height - _h - 5), text, font=FONT, fill='white')

        return im
