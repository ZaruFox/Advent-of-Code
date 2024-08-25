from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

genA = 516
genB = 190
res = 0

for _ in range(40_000_000):
    genA *= 16807
    genB *= 48271
    genA %= 2147483647
    genB %= 2147483647

    if genB & 65535 == genA & 65535:
        res += 1

print(res)