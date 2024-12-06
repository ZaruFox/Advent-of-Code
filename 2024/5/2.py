from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
from cv2 import bilateralFilter
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

# oh god

before = defaultdict(set)
for i, row in enumerate(data):
    if row == "":
        break

    a, b = row.split("|")
    before[int(b)].add(int(a))

res = 0
for row in data[i+1:]:
    nums = list(map(int, row.split(",")))
    valid = True

    prev = set()
    for num in nums:
        needed = before[num] & set(nums)

        if needed & prev != needed:
            valid = False
            break

        prev.add(num)

    if valid:
        continue

    correct = []
    while nums:
        for i in range(len(nums)):
            num = nums[i]
            needed = before[num] & set(nums)
            prev = set()

            if needed & prev == needed:
                nums.pop(i)
                prev.add(num)
                correct.append(num)
                break

    res += correct[len(correct)//2]

print(res)
