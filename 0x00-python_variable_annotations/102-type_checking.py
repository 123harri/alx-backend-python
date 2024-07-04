#!/usr/bin/env python3
"""
Type Checking
"""
from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zooms into the tuple by repeating each
    element according to the given factor.

    Args:
        lst (Tuple[int, ...]): The input tuple of integers.
        factor (int, optional): The zoom factor (default is 2).

    Returns:
        List[int]: The zoomed-in list where each
        element is repeated according to the factor.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
