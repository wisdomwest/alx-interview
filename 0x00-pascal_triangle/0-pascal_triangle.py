#!/usr/bin/python3
"""Module for pascal_triangle"""
from math import factorial


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    tri = []
    if n > 0:
        for i in range(1, n + 1):
            row = []
            val = 1
            for j in range(1, i + 1):
                row.append(val)
                val = val * (i - j) // j
            tri.append(row)
    return tri
