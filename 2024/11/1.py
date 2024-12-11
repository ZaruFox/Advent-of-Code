from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = [int(x) for x in f.read().strip().split()]

for _ in range(75):
    i = 0
    while i < len(data):
        strLen = len(str(data[i]))

        if data[i] == 0:
            data[i] = 1

        elif len(str(data[i])) % 2 == 0:
            oriStr = str(data[i])
            data[i] = int(oriStr[:strLen//2])
            data.insert(i+1, int(oriStr[strLen//2:]))
            i += 1

        else:
            data[i] *= 2024

        i += 1

print(len(data))