#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to create the function.

    Returns:
        Callable[[float], float]: A function that accepts
        a float and returns the multiplied result.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
