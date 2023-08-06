# imports
from PIL import Image
import os
from ImageEffects.constants import EMOJIS_DIR
from importlib import resources
import io


class _emojioverlay:
    '''Static class'''
    EMOJI_PADDING_VALUE = 5

    @classmethod
    def renderimage(cls, image: str, emoji: str = '', alpha: int = 100) -> Image.Image:
        im = Image.open(image)
        im = im.convert('RGBA')
        try:
            with resources.open_binary('resources.emojis', cls.getEmojiName(emoji)) as fp:
                _img = fp.read()
        except Exception:
            raise Exception(f"Emoji {emoji}' could not be found in the library. See available emojis: https://openmoji.org/")

        _emoji_file = io.BytesIO(_img)
        emoji_im = Image.open(_emoji_file)
        emoji_im = emoji_im.crop((cls.EMOJI_PADDING_VALUE, cls.EMOJI_PADDING_VALUE, emoji_im.width -
                                  cls.EMOJI_PADDING_VALUE, emoji_im.height - cls.EMOJI_PADDING_VALUE))
        emoji_im = emoji_im.resize((im.width, im.height))
        emoji_im = emoji_im.convert('RGBA')
        emoji_im.putalpha(alpha)

        im = Image.alpha_composite(im, emoji_im)
        return im

    @classmethod
    def getEmojiPath(cls, emoji: str = '') -> str:
        '''returns the emoji image of type Image'''
        _emoji_file_name = cls.getEmojiName(emoji)
        _emoji_file_path = os.path.join(EMOJIS_DIR, _emoji_file_name)
        return _emoji_file_path

    @classmethod
    def getEmojiName(cls, emoji: str = '') -> str:
        '''returns the emoji file name.'''
        _emoji_code = "-".join(f"{ord(c):x}" for c in emoji).upper()
        emoji_name = f"{_emoji_code}.png"
        return emoji_name
