from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = int(f.read().strip())

def getAdj(gridDict, cur, data):
    res = 0
    x, y = cur
    for adj in ((x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)):
        if adj in gridDict:
            res += gridDict[adj]
    
    # this is cursed
    if res > data:
        print(res)
        exit()
    
    print(cur, res)
    return res

gridDict = {(0, 0): 1}
cur = [0, 0]
length = 2
while True:
    cur[0] += 1
    gridDict[tuple(cur)] = getAdj(gridDict, cur, data)

    for _ in range(length-1):
        cur[1] -= 1
        gridDict[tuple(cur)] = getAdj(gridDict, cur, data)

    for _ in range(length):
        cur[0] -= 1
        gridDict[tuple(cur)] = getAdj(gridDict, cur, data)

    for _ in range(length):
        cur[1] += 1
        gridDict[tuple(cur)] = getAdj(gridDict, cur, data)

    for _ in range(length):
        cur[0] += 1
        gridDict[tuple(cur)] = getAdj(gridDict, cur, data)

    length += 2
    
    
    
