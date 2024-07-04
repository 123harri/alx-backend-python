#!/usr/bin/env python3
"""
This module provides a function to zoom into
an array by repeating its elements.
"""

from typing import List, Tuple


def zoom_array(lst: List, factor: int = 2) -> List:
    """
    Zooms into the array by repeating each
    element according to the given factor.

    Args:
        lst (List): The input list.
        factor (int, optional): The zoom factor (default is 2).

    Returns:
        List: The zoomed-in list where each element is
        repeated according to the factor.
    """
    zoomed_in = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
