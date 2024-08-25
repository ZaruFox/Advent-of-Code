from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

DIRECTIONS = {"U":-1j, "D":1j, "L":-1, "R":1}
KEYPADS = {2+0j: "1", 1+1j: "2", 2+1j: "3", 3+1j: "4", 2j: "5", 1+2j: "6", 2+2j: "7", 3+2j: "8", 4+2j: "9", 1+3j: "A", 2+3j: "B", 3+3j: "C", 2+4j: "D"}
curPos = 2j

code = ""
for instructions in data:
    for direction in instructions:
        newPos = curPos + DIRECTIONS[direction]

        if newPos in KEYPADS:
            curPos = newPos

    code += KEYPADS[curPos]

print(code)