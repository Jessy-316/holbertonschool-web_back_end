#!/usr/bin/env python3
"""
    Type annotated function which takes string (k) and an int or float (v)
    as arguments and returns a tuple with the first element being a str(k)
    and the second argument being an int or float (v)
    but being annotated as a float
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple with the str(k) and the square of int/float(v) """
    return (k, v ** 2)
