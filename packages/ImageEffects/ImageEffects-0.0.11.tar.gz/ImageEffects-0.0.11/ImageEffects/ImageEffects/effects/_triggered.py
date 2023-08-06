# imports
from PIL import Image
from importlib import resources
import io


class _triggered:
    '''Static class'''
    RED_BAND_INCREASE_RATIO = 1.5
    TRIGGER_TEMPLATE_FILENAME = 'trigger_meme_template.png'

    @classmethod
    def renderimage(cls, image: str) -> Image.Image:
        im = Image.open(image)
        r, g, b = im.split()
        r = r.point(lambda i: i * cls.RED_BAND_INCREASE_RATIO)
        im = Image.merge('RGB', (r, g, b))

        with resources.open_binary('resources.templates', cls.TRIGGER_TEMPLATE_FILENAME) as fp:
            _trigger_template = io.BytesIO(fp.read())
        _template_im = Image.open(_trigger_template)

        _trigger_template = _template_im.resize((im.width, int(15/100 * im.height)))

        im.paste(_trigger_template, (0, im.height - _trigger_template.height))

        return im
