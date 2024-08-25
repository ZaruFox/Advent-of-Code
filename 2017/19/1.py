from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

DIRECTIONS = [-1j, 1+0j, 1j, -1+0j]
curDir = 2
curPos = data[0].index("|") + 0j

def getVal(grid, position):
    if not (0 <= int(position.imag) < len(grid) and 0 <= int(position.real) < len(grid[0])):
        return " "
    return grid[int(position.imag)][int(position.real)]

res = ""
while True:
    if (val := getVal(data, curPos)) not in "|+-":
        res += val

    nextPos = curPos + DIRECTIONS[curDir]
    if getVal(data, nextPos) == " ":
        if getVal(data, curPos + DIRECTIONS[(curDir - 1) % 4]) != " ":
            curDir -= 1
            curDir %= 4
            curPos += DIRECTIONS[curDir]

        elif getVal(data, curPos + DIRECTIONS[(curDir + 1) % 4]) != " ":
            curDir += 1
            curDir %= 4
            curPos += DIRECTIONS[curDir]

        else:
            print(res)
            break
    else:
        curPos = nextPos
    