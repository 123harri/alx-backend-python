#!/usr/bin/env python3
"""This module contains a function that returns an
asyncio.Task for the wait_random coroutine."""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: A task that runs the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
