from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math

def checkSafe(nums):
    for i in range(1, len(nums)):
        if not 1 <= abs(nums[i]-nums[i-1]) <= 3:
            return False

    sortedNums = sorted(nums)
    return nums in (sortedNums, sortedNums[::-1])
        
with open("data.txt") as f:
    data = f.read().splitlines()

res = 0
for row in data:
    original = list(map(int, row.split()))

    for removed in range(-1, len(original)):
        nums = original.copy()
        if removed != -1:
            nums.pop(removed)
            
        if checkSafe(nums):
            res += 1
            break

print(res)