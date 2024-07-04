#!/usr/bin/env python3
"""
This module provides a function to safely
retrieve a value from a dictionary.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
        ) -> Union[Any, T]:
    """
    Safely retrieves the value associated with the key from the dictionary.
    Returns the default value if the key is not present in the dictionary.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to lookup in the dictionary.
        default (Union[T, None], optional): The default value to
        return if key is not found (default is None).

    Returns:
        Union[Any, T]: The value associated with the key in the
        dictionary, or the default value if key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
