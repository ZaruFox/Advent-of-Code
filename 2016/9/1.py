from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.readline().strip()

i = 0
extra = 0
while i < len(data):
    if data[i] == "(":
        i += 1
        marker = ""

        while data[i] != ")":
            marker += data[i]
            i += 1

        length, times = [int(x) for x in marker.split("x")]
        extra += length * (times-1) - (2 + len(marker))
        i += length + 1
    else:
        i += 1

print(len(data) + extra)