#!/usr/bin/python3
"""Module for pascal_triangle"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    # Create empty list
    tri = []
    # If n is less than 0, return an empty list
    if n > 0:
        # Loop through the range of n
        for i in range(1, n + 1):
            # Define row as an empty list
            row = []
            # Loop through the range of i
            val = 1
            # Loop through the range of j
            for j in range(1, i + 1):
                # Append the value of val to row
                row.append(val)
                # Update the value of val
                val = val * (i - j) // j
            # Append row to tri
            tri.append(row)
    # Return tri
    return tri
