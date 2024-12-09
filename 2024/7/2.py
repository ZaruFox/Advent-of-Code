from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

def isValid(target, i, nums, current=0):
    if i == len(nums):
        return current == target
    
    return isValid(target, i+1, nums, current+nums[i]) or \
    isValid(target, i+1, nums, current*nums[i]) or \
    isValid(target, i+1, nums, int(f"{current}{nums[i]}"))



with open("data.txt") as f:
    data = f.read().splitlines()

res = 0
for row in data:
    target, nums = row.split(": ")
    target = int(target)
    nums = [int(x) for x in nums.split()]

    if isValid(target, 0, nums):
        res += target

print(res)