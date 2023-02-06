#!/usr/bin/env python3
"""1. execute multiple coroutines at the same time with async"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes wait_random n times.
    """
    delay_time = [asyncio.create_task(wait_random(max_delay))
                  for _ in range(n)]
    return [await task for task in asyncio.as_completed(delay_time)]
