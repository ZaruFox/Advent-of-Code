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
numbers = [[data[i]%10] for i in range(len(data))]
for i, num in enumerate(data):
    for _ in range(2000):
        num ^= 64 * num
        num %= 16777216

        num ^= num // 32
        num %= 16777216

        num ^= 2048 * num
        num %= 16777216
        
        numbers[i].append(num%10)

changes = [{} for _ in range(len(data))]
allChanges = defaultdict(int)

for i, arr in enumerate(numbers):
    prevChanges = deque()
    for j, num in enumerate(arr):
        prevChanges.append(num - arr[j-1])

        if len(prevChanges) == 5:
            prevChanges.popleft()

        if len(prevChanges) == 4:
            tmp = tuple(prevChanges)
            if tmp not in changes[i]:
                changes[i][tmp] = num
                allChanges[tmp] += num

print(max(allChanges.values()))