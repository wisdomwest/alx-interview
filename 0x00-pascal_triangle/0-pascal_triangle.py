#!/usr/bin/python3
"""Module for pascal_triangle"""
from math import factorial


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    triangle = []

    for i in range(n):
        row = []
        for j in range(n - i + 1):
            row.append(" ")
        for j in range(i + 1):
            # nCr = n!/((n-r)!*r!)
            row.append(factorial(i) // (factorial(j) * factorial(i - j)))
        triangle.append(row)
    return triangle
