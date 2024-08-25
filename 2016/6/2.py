from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

res = [defaultdict(int) for _ in range(len(data[0]))]

for msg in data:
    for i in range(len(msg)):
        res[i][msg[i]] += 1


print("".join([min(counts.keys(), key=lambda x: counts[x]) for counts in res]))