from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy
import hashlib

VAULTSIZE = 3

def getMD5(string: str):
    return hashlib.md5(string.encode()).hexdigest()

with open("data.txt") as f:
    data = f.readline().strip()

queue = deque([(0, 0, "")])

while queue:
    x, y, path = queue.popleft()

    if (x, y) == (VAULTSIZE, VAULTSIZE):
        print(path)
        break

    md5Hash = getMD5(f"{data}{path}")
    for hash_, direction, newX, newY in ((md5Hash[0], "U", x, y-1), (md5Hash[1], "D", x, y+1), (md5Hash[2], "L", x-1, y), (md5Hash[3], "R", x+1, y)):
        if not (0 <= newX <= VAULTSIZE and 0 <= newY <= VAULTSIZE) or hash_ not in "bcdef":
            continue

        queue.append((newX, newY, path + direction))
