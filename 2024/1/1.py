from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

a1 = []
a2 = []

for row in data:
    num1, num2 = map(int, row.split())
    a1.append(num1)
    a2.append(num2)

a1.sort()
a2.sort()
res = 0

for i in range(len(a1)):
    res += abs(a1[i] - a2[i])

print(res)

    