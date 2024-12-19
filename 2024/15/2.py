from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

def checkValid(x, y, dx, dy):
    newX = dx+x
    newY = dy+y

    if (newX, newY) in walls or (newX+1, newY) in walls:
        return False, set()
    
    res = True
    movedBoxes = set()
    for i in range(-1, 2):
        if dx != 0 and dx == -i:
            continue

        if (newX+i, newY) in boxes:
            valid, newBoxes = checkValid(newX+i, newY, dx, dy)
            res &= valid
            movedBoxes |= newBoxes

    return res, movedBoxes | {(x, y)}

with open("data.txt") as f:
    grid, instructions = f.read().split("\n\n")
    grid = [list(x) for x in grid.splitlines()]
    instructions = "".join(instructions.splitlines())

DIRECTIONS = {"^": (0, -1), ">": (1, 0), "<": (-1, 0), "v": (0, 1)}
boxes = set()
walls = set()

for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == "@":
            curX = x*2
            curY = y*2

        elif char == "O":
            boxes.add((x*2, y*2))

        elif char == "#":
            walls.add((x*2, y*2))


for dx, dy in map(lambda x: DIRECTIONS[x], instructions):
    valid = True
    movedBoxes = set()

    if (curX+dx, curY+dy) in walls:
        continue

    if (curX+dx, curY+dy) in boxes:
        valid, movedBoxes = checkValid(curX+dx, curY+dy, dx, dy)
    elif (curX+dx-1, curY+dy) in boxes:
        valid, movedBoxes = checkValid(curX+dx-1, curY+dy, dx, dy)

    if valid:
        curX += dx
        curY += dy

        boxes ^= movedBoxes
        boxes |= set((x+dx, y+dy) for x, y in movedBoxes)

        
print(sum(y*100+x for x, y in boxes))