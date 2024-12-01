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

count = Counter(a2)
res = 0
for num in a1:
    res += num * count[num]

print(res)