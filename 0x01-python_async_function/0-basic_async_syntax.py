#!/usr/bin/env python3
'''
an asynchronous coroutine
'''
import random
import asyncio


async def wait_random(max_delay=int(10)):
    timer = random.uniform(0, float(max_delay))
    await asyncio.sleep(timer)
    return timer
