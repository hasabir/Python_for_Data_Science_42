import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''The unction that takes as parameters a 2D array,\
         prints its shape, and returns a\
         truncated version of the array based on the\
         provided start and end arguments.\
         You must use the slicing method'''
    try:
        print(f'My shape is : {np.array(family).shape}')
        if not isinstance(family, list) or not isinstance(start, int)\
                or not isinstance(end, int):
            raise TypeError('accepted args [list] [int] [int]')
        result = family[start: end]
        print(f'My new shape is : {np.array(result).shape}')
    except Exception as err:
        print('Error:', err)
        return
    return result
