from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    memory = [int(x) for x in f.read().splitlines()[0].split()]

visited = set()
counter = 0

while tuple(memory) not in visited:
    visited.add(tuple(memory))

    i = max(range(len(memory)), key = lambda x: (memory[x], -x))

    toDistribute, memory[i] = memory[i], 0

    while i+1 < len(memory):
        toDistribute -= 1
        i += 1
        memory[i] += 1

    div, mod = divmod(toDistribute, len(memory))

    for j in range(len(memory)):
        if j < mod:
            memory[j] += 1
        memory[j] += div

    counter += 1

print(counter)