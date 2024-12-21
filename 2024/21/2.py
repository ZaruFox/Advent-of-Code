from collections import deque, defaultdict, Counter
import re
from functools import cache, reduce
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

numberPad = [["7", "8", "9"],
             ["4", "5", "6"],
             ["1", "2", "3"],
             ["#", "0", "A"]]

directionPad = [["#", "^", "A"],
                ["<", "v", ">"]]

DIRECTIONS = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">":(1, 0)}

def pathToCounter(path, step=1):
    c = Counter()
    c[f"A{path[0]}"] += step
    for i in range(1, len(path)):
        c[f"{path[i-1]}{path[i]}"] += step
    return c 

def getDirections(pad, target, i):
    if i == len(target):
        return [Counter()]
    
    for y1, row in enumerate(pad):
        for x1, char in enumerate(row):
            if char == target[i][0][1]:
                finalX, finalY = x1, y1
            if char == target[i][0][0]:
                x, y = x1, y1

    validRoutes = []
    dx, dy = finalX - x, finalY - y

    validRoutes.append(abs(dx) * (">" if dx > 0 else "<") + abs(dy) * ("v" if dy > 0 else "^"))
    if dx != 0 and dy != 0:
        validRoutes.append(validRoutes[0][::-1])

        if pad[finalY][x] == "#":
            validRoutes.pop()
        elif pad[y][finalX] == '#' or (validRoutes[0] and validRoutes[0][0] == ">"):
            validRoutes.pop(0)

    validRoutes = [x + "A" for x in validRoutes]

    validCounter = []
    for route in validRoutes:
        validCounter.append(pathToCounter(route, target[i][1]))

    res = itertools.product(validCounter, getDirections(pad, target, i+1))
    return [a+b for a, b in res]

res = 0
for i in range(len(data)):
    tmp = getDirections(numberPad, list(pathToCounter(data[i]).items()), 0)

    for _ in range(25):
        tmp = reduce(lambda a,b:a+b, [getDirections(directionPad, tuple(x.items()), 0) for x in tmp])

        minLength = min(sum(x.values()) for x in tmp)
        tmp = [x for x in tmp if sum(x.values()) == minLength]

    res += int(data[i][:-1]) * min(sum(x.values()) for x in tmp)

print(res)
