from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().strip()

for _ in range(50):
    new = [[data[0], 1]]
    for char in data[1:]:
        if char == new[-1][0]:
            new[-1][1] += 1
        else:
            new.append([char, 1])

    data = "".join([f"{x[1]}{x[0]}" for x in new])

print(len(data))