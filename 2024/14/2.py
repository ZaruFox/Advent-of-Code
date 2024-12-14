from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

robots = []

n = 103
m = 101

for line in data:
    robots.append([int(x) for x in re.split(r",| v=", line.strip("p="))])

def getScore(steps):
    pos = set()
    score = 0

    for x, y, dx, dy in robots:
        newX = (x + dx*steps) % m
        newY = (y + dy*steps) % n
        
        pos.add((newX, newY))
        for x1, y1 in ((newX+1, newY), (newX-1, newY), (newX, newY-1), (newX, newY+1)):
            if (x1, y1) in pos:
                score += 1

    return pos, score

def display(pos):
    pos = set(pos)
    for y in range(n):
        for x in range(m):
            if (x, y) in pos:
                print("#", end="")
            else:
                print(".", end="")

        print()

steps = 0
while True:
    pos, score = getScore(steps)

    if score >= 500:
        display(pos)
        print(steps, score)
        break

    steps += 1

        
