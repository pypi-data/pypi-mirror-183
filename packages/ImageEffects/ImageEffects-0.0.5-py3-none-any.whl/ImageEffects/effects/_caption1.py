# imports
from PIL import Image, ImageDraw, ImageFont
from importlib import resources
import io


class _caption1:
    '''Static class'''
    TEXT_COLOR = (255, 255, 255)
    FONT_SIZE_RATIO = 10/100  # 10%
    LINE_LENGTH = int(FONT_SIZE_RATIO * 100 * 1.5)

    @classmethod
    def renderimage(cls, image: str, text: str = 'text here') -> Image.Image:
        if len(text) == 0:
            text = 'text here'

        with resources.open_binary('resources.fonts', 'impact.ttf') as fp:
            _font_file = io.BytesIO(fp.read())

        im = Image.open(image)
        IMPACT_FONT = ImageFont.truetype(_font_file, int(cls.FONT_SIZE_RATIO * im.width))
        editable_im = ImageDraw.Draw(im)
        X_DISTANCE = im.width - (85/100 * im.width)
        editable_im.text((X_DISTANCE, 5), cls.format_text(text), cls.TEXT_COLOR, font=IMPACT_FONT)

        return im

    @classmethod
    def format_text(cls, text: str) -> str:
        '''takes the input string and formats if its longer than the threshold length'''
        if len(text) > cls.LINE_LENGTH:

            _text_list = []
            _temp_length = 0
            _temp_list = []

            _word_list = text.split(' ')

            for _each_word in _word_list:
                _temp_length += len(_each_word)
                _temp_list.append(_each_word)

                if _temp_length > cls.LINE_LENGTH:
                    _text_list.append(" ".join(_temp_list))
                    _temp_list = []
                    _temp_length = 0

            if len(_temp_list) > 0:
                _text_list.append(' '.join(_temp_list))

            _text = '\n'.join(_text_list)

            return _text

        return text
