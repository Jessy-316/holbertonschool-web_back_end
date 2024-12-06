#!/usr/bin/env python3
"""File that contains a function that returns an asyncio.Task"""
import asyncio
wR = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function that returns an asyncio.Task of the wait_random"""

    return asyncio.create_task(wR(max_delay))
