#!/usr/bin/env python3
"""
This module provides a function to create a
tuple with a string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is
    a string and the second element
    is the square of the given number (int or float).

    Args:
        k (str): The string.
        v (Union[int, float]): The number to be squared.

    Returns:
        Tuple[str, float]: A tuple containing the
        string and the square of the number.
    """
    return (k, float(v ** 2))
