from collections import defaultdict
from itertools import cycle
import math

adjDict = defaultdict(list)
curNodes = []
with open("data.txt") as f:
    directions = list(f.readline().strip())
    f.readline()

    for line in f:
        if line[2] == "A":
            curNodes.append(line[0:3])
        adjDict[line[0:3]] = [line[7:10], line[12:15]]

stepsToZ = defaultdict(int)
for start in curNodes:
    cur = start
    count = 0
    for direction in cycle(directions):
        if cur[-1] == "Z":
            stepsToZ[start] = count
            break

        if direction == "L":
            cur = adjDict[cur][0]
        else:
            cur = adjDict[cur][1]
        count += 1

print(math.lcm(*stepsToZ.values()))
