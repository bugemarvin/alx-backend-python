#!/usr/bin/env python3
""" 6. Complex types - mixed list
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ Computes the sum of a list of integers and floating-point numbers.
    """
    return sum(mxd_list)
