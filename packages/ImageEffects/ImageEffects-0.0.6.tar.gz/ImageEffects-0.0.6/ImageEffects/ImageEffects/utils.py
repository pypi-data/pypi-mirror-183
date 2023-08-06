def map_(value: int, input_start: int, input_stop: int, output_start: int, output_stop: int) -> float:
    '''Takes a value between `input_start` and `input_stop` as `value`
    returns the value it maps between `output_start` and `output_stop`'''
    return output_start + (output_stop - output_start) * ((value - input_start) / (output_stop - input_start))
