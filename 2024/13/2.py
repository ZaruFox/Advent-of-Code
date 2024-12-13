from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

def solve(target, a, b):
    ans = 0
    while target[0] % b[0] != 0 or target[1] % b[1] != 0 or target[0] // b[0] != target[1] // b[1]:
        target[0] -= a[0]
        target[1] -= a[1]
        ans += 3

        if target[0] < 0 and target[1] < 0:
            return math.inf
    return ans + target[0] // b[0]

with open("data.txt") as f:
    data = f.read().splitlines()

# when you dont know linear algebra:

res = 0
for i in range(0, len(data), 4):
    a = [int(x) for x in re.split(r"Button A: X\+|, Y\+", data[i])[1:]]
    b = [int(x) for x in re.split(r"Button B: X\+|, Y\+", data[i+1])[1:]]
    target = [int(x) for x in re.split(r"Prize: X=|, Y=", data[i+2])[1:]]

    if ((a[1] > a[0]) and (b[1] > b[0])) or ((a[1] < a[0]) and (b[1] < b[0])):
        continue

    ans = 0
    aDiff = abs(a[1]-a[0])
    bDiff = abs(b[1]-b[0])
    padding = 100000

    dx = bDiff * a[0] + aDiff * b[0]
    count, rem = divmod(10000000000000-padding, dx)
    ans += count * (bDiff * 3 + aDiff)
    target = [target[0] + padding + rem, target[1] + padding + rem]

    ans += solve(target, a, b)
    res += ans if ans != math.inf else 0

print(res)