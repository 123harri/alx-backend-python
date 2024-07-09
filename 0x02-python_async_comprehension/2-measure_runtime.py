#!/usr/bin/env python3
"""
This module provides a function to measure the runtime of
executing async comprehensions in parallel.
"""
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in
    parallel and measures the total runtime.

    Returns:
        float: The total runtime of the executions.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
