#!/usr/bin/python3
""" Creates a function that calculates perimeter of an island"""


def island_perimeter(grid):
    """ Calculates perimeter of a grid
    returns perimeter of integer"""

    width = 1
    height = 0
    maxw = -101
    for i in range(1, len(grid) - 1):
        for j in  range(1, len(grid[i]) - 1):
            if grid[i][j] == 1 and grid[i][j + 1] == 1:
                width += 1
        if width >= 1 and width > maxw:
            maxw = width;
    width = 1;
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] == 1 and grid[i][j + 1] != 1:
                height += 1
    return maxw * 2 + height * 2
