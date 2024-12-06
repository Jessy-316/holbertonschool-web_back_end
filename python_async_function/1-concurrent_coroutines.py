#!/usr/bin/env python3
"""A file that contains a wait_n function."""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times and returns the list of delays in ascending order.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    # Create a list of asyncio tasks
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    delays = []
    for task in asyncio.as_completed(tasks):
        result = await task
        # Insert into the list in ascending order without using sort()
        for i in range(len(delays)):
            if result < delays[i]:
                delays.insert(i, result)
                break
        else:
            delays.append(result)

    return delays
