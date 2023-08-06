def map_(value: int, input_start: int, input_stop: int, output_start: int, output_stop: int) -> float:
    '''Takes a value between `input_start` and `input_stop` as `value`
    returns the value it maps between `output_start` and `output_stop`'''
    return output_start + (output_stop - output_start) * ((value - input_start) / (output_stop - input_start))


def format_text(_line_length: int = 21, text: str = 'text here') -> str:
    '''takes the input string and formats if its longer than the threshold length'''
    if len(text) > _line_length:

        _text_list = []
        _temp_length = 0
        _temp_list = []

        _word_list = text.split(' ')

        for _each_word in _word_list:
            _temp_length += len(_each_word)
            _temp_list.append(_each_word)

            if _temp_length > _line_length:
                _text_list.append(" ".join(_temp_list))
                _temp_list = []
                _temp_length = 0

        if len(_temp_list) > 0:
            _text_list.append(' '.join(_temp_list))

        _text = '\n'.join(_text_list)

        return _text

    return text
