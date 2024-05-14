#!/usr/bin/python3
"""
file for Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle
    """
    result = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            Count = 1
            for j in range(1, i + 1):
                level.append(Count)
                Count = Count * (i - j) // j
            result.append(level)
    return result
