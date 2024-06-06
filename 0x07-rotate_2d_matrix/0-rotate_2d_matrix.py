#!/usr/bin/python3
"""
function rotates an nxn 2D matrix 90 degrees clockwise in-place
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2d square matrix 90 degrees clockwise
    Args:
        matrix (list): 2d square matrix
    Return:
        None
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(n):
        for j in range(int(n / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = temp