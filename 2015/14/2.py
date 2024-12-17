from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

scores = [0] * len(data)

for totalTime in range(1, 2504):
    winners = []
    maxDist = 0

    for i, line in enumerate(data):
        speed, time, rest = [int(x) for x in re.findall(r"\d+", line)]

        cycleCount, remaining = divmod(totalTime, time+rest)
        dist = cycleCount * (speed*time) + speed * min(remaining, time)

        if dist == maxDist:
            winners.append(i)
        elif dist > maxDist:
            winners = [i]
            maxDist = dist

    for i in winners:
        scores[i] += 1

print(max(scores))

