#!/usr/bin/env python3
"""A file that contains a wait"""
from typing import List
wR = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """A function that waits for n random times"""
    delays = []

    for x in range(n):
        delay = await wR(max_delay)
        delays.append(delay)

    for i in range(1, len(delays)):
        key = delays[i]
        j = i - 1
        while j >= 0 and key < delays[j]:
            delays[j + 1] = delays[j]
            j -= 1
        delays[j + 1] = key

    return delays
