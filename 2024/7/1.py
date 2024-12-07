from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

def isValid(target, i, nums):
    if i == -1:
        return target == 0

    return isValid(target-nums[i], i-1, nums) or (isValid(target // nums[i], i-1, nums) if target % nums[i] == 0 else False)

with open("data.txt") as f:
    data = f.read().splitlines()

res = 0
for row in data:
    target, nums = row.split(": ")
    target = int(target)
    nums = [int(x) for x in nums.split()]

    if isValid(target, len(nums)-1, nums):
        res += target

print(res)