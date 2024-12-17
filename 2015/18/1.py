from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

on = set()
for y, row in enumerate(data):
    for x, char in enumerate(row):
        if char == "#":
            on.add((x, y))

for _ in range(100):
    newOn = set()

    for y in range(len(data)):
        for x in range(len(data[0])):
            directions = ((x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1))
            adjOn = sum((adjX, adjY) in on for adjX, adjY in directions)

            if adjOn in (2, 3) and (x, y) in on:
                newOn.add((x, y))
            elif adjOn == 3 and (not (x, y) in on):
                newOn.add((x, y))

    on = newOn

print(len(on))