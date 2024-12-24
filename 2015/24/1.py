from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = [int(x) for x in f.read().splitlines()]


data = set(data)
target = sum(data) // 3
count = 1
while True:
    validComs = []
    for com in itertools.combinations(data, count):
        if target != sum(com):
            continue

        count2 = 0
        valid = False
        tmp = data ^ set(com)
        while count2 < len(tmp):
            for com2 in itertools.combinations(tmp, count2):
                if sum(com2) == target:
                    valid = True
                    break

            if valid:
                break
            count2 += 1

        validComs.append(com)

    if validComs:
        print(validComs)
        print(min(map(math.prod, validComs)))
        break
    count += 1

