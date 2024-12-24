from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = [int(x) for x in f.read().splitlines()]


def isValid(depth, target, nums):
    if depth == 2:
        return True
    
    count2 = 0
    while count2 < len(nums):
        for com2 in itertools.combinations(nums, count2):
            if sum(com2) == target and isValid(depth+1, target, nums ^ set(com2)):
                return True
            
        count2 += 1

    return False


data = set(data)
target = sum(data) // 4
count = 1
while True:
    validComs = []
    for com in itertools.combinations(data, count):
        if target != sum(com):
            continue

        if isValid(0, target, data ^ set(com)):
           validComs.append(com)

    if validComs:
        print(validComs)
        print(min(map(math.prod, validComs)))
        break
    count += 1

