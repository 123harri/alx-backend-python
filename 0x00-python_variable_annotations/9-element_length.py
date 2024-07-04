#!/usr/bin/env python3
"""
This module provides a function to return
tuples of elements and their lengths.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing elements and their lengths.

    Args:
        lst (Iterable[Sequence]): The input list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where
        each tuple contains an element and its length.
    """
    return [(i, len(i)) for i in lst]
