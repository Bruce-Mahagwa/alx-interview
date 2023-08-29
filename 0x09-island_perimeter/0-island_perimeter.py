#!/usr/bin/python3
""" Creates a function that calculates perimeter of an island"""


def island_perimeter(grid):
    """ Calculates perimeter of a grid
    returns perimeter of integer"""

    """width = 1
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
    return maxw * 2 + height * 2"""
    count = 0
    row = len(grid)
    col = len(grid[0]) if row else 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            idx = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
            check = [1 if k[0] in range(row) and k[1] in range(col) else 0
               for k in idx]

            if grid[i][j]:
                count += sum([1 if not r or not grid[k[0]][k[1]] else 0
                    for r, k in zip(check, idx)])
    return (count)
