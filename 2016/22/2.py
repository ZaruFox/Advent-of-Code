from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

def getPath(startPos, endPos, inaccessible, n, dataPos):
    queue = deque([startPos])
    visited = {startPos: None}

    while queue:
        x, y = queue.popleft()

        for newX, newY in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if not (0 <= newX <= n and 0 <= newY <= n) or (newX, newY) in visited or (newX, newY) in inaccessible or (newX, newY) == dataPos:
                continue

            visited[(newX, newY)] = (x, y)

            if (newX, newY) == endPos:
                break

            queue.append((newX, newY))

    res = []
    while visited[endPos]:
        res.append(endPos)
        endPos = visited[endPos]
    
    return res[::-1]
        

n = 30
blankPos = ()
inaccessible = set()
dataPos = (n, 0)

with open("data.txt") as f:
    for line in f:
        # get all integer values
        nodeData = re.split("/dev/grid/node-x|-y|T? +|%\n?", line)

        # convert all values to int and removes empty strings
        x, y, _, used, _, _ = [int(x) for x in nodeData if x]

        if used == 0:
            blankPos = (x, y)

        elif used > 200:
            inaccessible.add((x, y))

result = 0
for targetPos in getPath(dataPos, (0, 0), inaccessible, n, dataPos):
    result += len(getPath(blankPos, targetPos, inaccessible, n, dataPos)) + 1
    blankPos, dataPos = dataPos, targetPos

print(result)
