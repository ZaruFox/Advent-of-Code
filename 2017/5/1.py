from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

instructions = [int(x) for x in data]
pointer = 0
count = 0

while pointer < len(instructions):
    instructions[pointer], pointer = instructions[pointer]+1, pointer + instructions[pointer]
    count += 1

print(count)