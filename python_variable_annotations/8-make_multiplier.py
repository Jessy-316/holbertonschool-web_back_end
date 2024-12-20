#!/usr/bin/env python3
"""
    Type annotated function which takes a float (multiplier) as argument
    and returns a function that multiplies a float by multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float by multiplier """
    def mul(x: float) -> float:
        """ Multiplies a float by multiplier """
        return x * multiplier
    return mul
