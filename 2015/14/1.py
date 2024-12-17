from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

maxDist = 0
totalTime = 2503
for line in data:
    speed, time, rest = [int(x) for x in re.findall(r"\d+", line)]

    cycleCount, remaining = divmod(totalTime, time+rest)
    maxDist = max(maxDist, cycleCount * (speed*time) + speed * min(remaining, time))

print(maxDist)

