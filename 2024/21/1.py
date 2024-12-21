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

memo = {}
def getDirections(pad, target, x, y, i):
    if i == len(target):
        return [""]
    
    if (pad[0][0], target[i], x, y) in memo:
        validRoutes, finalX, finalY = memo[(pad[0][0], target[i], x, y)]

    else:
        queue = deque([(x, y, "", set())])
        validRoutes = []

        while queue:
            curX, curY, steps, visited = queue.popleft()

            if pad[curY][curX] == target[i] and ((not validRoutes) or len(steps)+1 == len(validRoutes[-1])):
                validRoutes.append(steps + "A")
                finalX, finalY = curX, curY
                continue

            for symbol, (dx, dy) in DIRECTIONS.items():
                newX = curX + dx
                newY = curY + dy

                if not (0 <= newY < len(pad) and 0 <= newX < len(pad[0])) or pad[newY][newX] == "#":
                    continue

                if (newX, newY) in visited:
                    continue

                queue.append((newX, newY, steps + symbol, visited | {(newX, newY)}))

        memo[(pad[0][0], target[i], x, y)] = (validRoutes, finalX, finalY)

    res = itertools.product(validRoutes, getDirections(pad, target, finalX, finalY, i+1))
    return [a+b for a, b in res]

res = 0
for i in range(len(data)):
    tmp = getDirections(numberPad, data[i], 2, 3, 0)
    tmp = reduce(lambda a,b:a+b, [getDirections(directionPad, x, 2, 0, 0) for x in tmp])
    tmp = reduce(lambda a,b:a+b, [getDirections(directionPad, x, 2, 0, 0) for x in tmp])

    res += int(data[i][:-1]) * min(len(x) for x in tmp)

print(res)
