#!/usr/bin/env python3
"""
This module provides a function to safely
retrieve the first element of a list.
"""

from typing import Sequence, TypeVar, Union

# Define a type variable T
T = TypeVar('T')


def safe_first_element(lst: Sequence[T]) -> Union[T, None]:
    """
    Safely returns the first element of the list,
    or None if the list is empty.

    Args:
        lst (Sequence): The input list.

    Returns:
        Union[T, None]: The first element of the list
        or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
