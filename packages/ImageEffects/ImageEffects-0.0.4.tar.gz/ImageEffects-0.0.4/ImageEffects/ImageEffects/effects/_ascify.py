# imports
from art import text2art


class _ascify:
    '''Static class'''
    @staticmethod
    def renderimage(text: str = 'ascify') -> str:
        return text2art(text, font='straight')
