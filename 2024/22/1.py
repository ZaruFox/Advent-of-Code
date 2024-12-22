from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = [int(x) for x in f.read().splitlines()]

res = 0
for num in data:
    for _ in range(2000):
        num ^= 64 * num
        num %= 16777216

        num ^= num // 32
        num %= 16777216

        num ^= 2048 * num
        num %= 16777216

    res += num

print(res)