#!/usr/bin/python3
"""Rotates a 2d matric"""


def rotate_2d_matrix(matrix):
    """Rtates a 2d matrix in place
    returns nothing"""
    temp = []
    for i in range(0, len(matrix)):
        arr = []
        for j in range(len(matrix[i]) - 1, -1, -1):
            arr.append(matrix[j][i])
        temp.append(arr)
    for k in range(0, len(matrix)):
        matrix[k] = temp[k]
