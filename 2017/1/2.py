from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().strip("\n")

res = 0
for i in range(len(data)):
    if data[i] == data[(i+len(data) // 2) % len(data)]:
        res += int(data[i])

print(res)