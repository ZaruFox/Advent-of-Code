from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

def rotate(grid):
    return [[grid[y][x] for y in range(len(grid))] for x in range(len(grid[0]))]

with open("data.txt") as f:
    data = f.read().splitlines()

grid = [[0]*50 for _ in range(6)]

for instruction in data:
    if instruction.startswith("rect "):
        width, height = instruction.lstrip("rect ").split("x")

        for y in range(int(height)):
            for x in range(int(width)):
                grid[y][x] = 1


    elif instruction.startswith("rotate row y="):
        y, degree = instruction.strip("rotate row y=").split(" by ")

        grid[int(y)] = numpy.roll(grid[int(y)], int(degree))

    else:
        x, degree = instruction.strip("rotate column x=").split(" by ")

        grid = rotate(grid)
        grid = rotate(grid)
        grid = rotate(grid)
        grid[int(x)] = numpy.roll(grid[int(x)], int(degree))
        grid = rotate(grid)

for y in range(6):
    for x in range(50):
        if grid[y][x] == 0:
            print(".", end="")
        else:
            print("#", end="")

    print()