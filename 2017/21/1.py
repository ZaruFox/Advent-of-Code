from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

def rotate(matrix):
    return [[matrix[y][x] for y in range(len(matrix)-1, -1, -1)] for x in range(len(matrix))]

def xFlip(matrix):
    return matrix[::-1]

def yFlip(matrix):
    return [x[::-1] for x in matrix]

def matrixToString(matrix):
    return "".join(["".join(x) for x in matrix])

with open("data.txt") as f:
    data = f.read().splitlines()

schematic = {}
for line in data:
    key, val = line.split(" => ")
    key = [list(x) for x in key.split("/")]
    val = [list(x) for x in val.split("/")]

    for _ in range(4):
        schematic[matrixToString(key)] = val
        schematic[matrixToString(xFlip(key))] = val
        schematic[matrixToString(yFlip(key))] = val
        schematic[matrixToString(xFlip(yFlip(key)))] = val

        key = rotate(key)

curPaint = [[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]]
size = 3

for cycle in range(5):
    squareSize = 3 if size % 2 == 1 else 2
    newPaint = [[] for _ in range(size + size // squareSize)]

    for y in range(0, size, squareSize):
        for x in range(0, size, squareSize):
            newSchem = schematic[matrixToString([[curPaint[y2][x2] for x2 in range(x, x+squareSize)] for y2 in range(y, y+squareSize)])]

            for y2 in range(len(newSchem)):
                newPaint[y+y2+(y//squareSize)] += newSchem[y2]

    size += size // squareSize
    curPaint = newPaint

print(sum([x.count("#") for x in curPaint]))




