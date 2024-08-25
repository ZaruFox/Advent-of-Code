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

for _ in range(5_000_000):
    if _ % 100_000 == 0:
        print((_*100)/5_000_000, "%", sep="")
    while True:
        genA *= 16807
        genA %= 2147483647

        if genA % 4 == 0:
            break

    while True:
        genB *= 48271
        genB %= 2147483647

        if genB % 8 == 0:
            break

    if genB & 65535 == genA & 65535:
        res += 1

print(res)