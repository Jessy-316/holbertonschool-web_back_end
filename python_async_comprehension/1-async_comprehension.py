#!/usr/bin/env python3
""" File that contains the function async comprehension """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Function that returns a list of randomly generated floats """
    return [number async for number in async_generator()]
