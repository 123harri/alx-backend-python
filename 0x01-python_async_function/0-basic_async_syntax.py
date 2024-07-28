#!/usr/bin/env python3
"""This module contains an asynchronous coroutine
that waits for a random delay."""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay
    seconds and return the delay.

    Args:
        max_delay (int): The maximum number of seconds to wait.

    Returns:
        float: The actual delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
