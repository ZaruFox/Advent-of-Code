from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

vars = defaultdict(int)
res = -math.inf

for line in data:
    instruction, condition = line.split(" if ")

    condition = condition.split(" ")
    if eval(f"vars[\"{condition[0]}\"] {condition[1]} {condition[2]}"):
        instruction = instruction.split(" ")
        if instruction[1] == "dec":
            vars[instruction[0]] -= int(instruction[2])
        else:
            vars[instruction[0]] += int(instruction[2])

    res = max(*vars.values(), res)

print(res)