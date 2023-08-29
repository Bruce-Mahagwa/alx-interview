#!/usr/bin/python3
""" Calculates values of the pascal triangle and returns a list """


def pascal_triangle(n):
    """ Calucaltes values of the pascal triangle and returns a list"""
    if n <= 0:
        return ([])

    triangle = [[1]]
    for i in range(1, n):
        temp = [1]
        prev = triangle[i - 1]
        for j in range(len(prev)):
            curr = prev[j] + prev[j + 1] if j != len(prev) - 1 else 1
            temp.append(curr)

        triangle.append(temp)

    return triangle
