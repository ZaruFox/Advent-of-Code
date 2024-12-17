from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

target = Counter({"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1})

with open("data.txt") as f:
    data = f.read().splitlines()

for line in data:
    line = line.strip("Sue ")
    colonPos = line.index(":")
    i, stats = line[:colonPos], line[colonPos+2:]
    valid = True

    for stat in stats.split(", "):
        key, value = stat.split(": ")
        value = int(value)

        if key in ('cats', 'trees'):
            if value <= target[key]:
                valid = False
                break
        
        elif key in ('pomeranians', 'goldfish'):
            if value >= target[key]:
                valid = False
                break

        elif target[key] != value:
            valid = False
            break

    if valid:
        print(i)