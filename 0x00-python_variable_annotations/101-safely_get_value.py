#!/usr/bin/env python3
""" 11. More involved type annotations
"""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Retrieves a value from a dict using a given key.
    """
    if key in dct:
        return dct[key]
    else:
        return default
