#!/usr/bin/env python3
"""
    Type annotated function which takes a list
    (mxd_list) of integers and floats,
    and returns their sum as a float
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ Returns the sum of a list as a float """
    return sum(mxd_list)
