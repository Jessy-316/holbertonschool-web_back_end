#!/usr/bin/env python3
"""
    Type annotated function which takes a list (input_list),
    and returns their sum as a float
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Returns the sum of a list of floats """
    return sum(input_list)
