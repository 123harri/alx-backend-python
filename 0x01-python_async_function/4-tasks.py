#!/usr/bin/env python3
"""This module contains a function that spawns
multiple task_wait_random tasks."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times and returns a sorted list of wait times.

    Args:
        n (int): The number of times to call task_wait_random.
        max_delay (int): The maximum delay for task_wait_random.

    Returns:
        List[float]: A sorted list of wait times.
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
