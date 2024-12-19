from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    grid, instructions = f.read().split("\n\n")
    grid = [list(x) for x in grid.splitlines()]
    n, m = len(grid), len(grid[0])
    instructions = "".join(instructions.splitlines())

DIRECTIONS = {"^": (0, -1), ">": (1, 0), "<": (-1, 0), "v": (0, 1)}

for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == "@":
            curX = x
            curY = y

for dx, dy in map(lambda x: DIRECTIONS[x], instructions):
    valid = False
    tmpX = curX + dx
    tmpY = curY + dy

    while 0 <= tmpX < m and 0 <= tmpY < n and grid[tmpY][tmpX] != "#":
        if grid[tmpY][tmpX] == ".":
            valid = True
            break

        tmpX += dx
        tmpY += dy

    if valid:
        while tmpX != curX or tmpY != curY:
            grid[tmpY][tmpX] = grid[tmpY-dy][tmpX-dx]

            tmpX -= dx
            tmpY -= dy

        grid[tmpY][tmpX] = "."
        curX += dx
        curY += dy

print(sum(sum(y*100 + x for x, char in enumerate(row) if char == "O") for y, row in enumerate(grid)))