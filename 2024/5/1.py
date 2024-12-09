from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

def checkValid(nums):
    prev = set()
    numsSet = set(nums)

    for num in nums:
        if before[num] & numsSet != prev:
            return False

        prev.add(num)

    return True

before = defaultdict(set)
for i, row in enumerate(data):
    if row == "":
        break

    a, b = [int(x) for x in row.split("|")]
    before[b].add(a)

res = 0
for row in data[i+1:]:
    nums = [int(x) for x in row.split(",")]

    if checkValid(nums):
        res += nums[len(nums)//2]

print(res)
