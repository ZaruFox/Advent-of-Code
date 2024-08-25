from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

DISKSIZE = 35651584

with open("data.txt") as f:
    data = list([int(x) for x in f.readline().strip()])

while len(data) < DISKSIZE:
    data += [0] + [(x+1)%2 for x in data[::-1]]
data = data[:DISKSIZE]

while len(data) % 2 == 0:
    checksum = []
    for i in range(0, len(data), 2):
        checksum.append((data[i] ^ data[i+1] + 1) % 2)
    data = checksum

print("".join([str(x) for x in data]))