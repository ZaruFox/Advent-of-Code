from collections import deque, defaultdict
from statistics import mode
import re
from functools import cache
import itertools
from statistics import mode
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

adjDict = defaultdict(lambda: [-1, [], []])
validDict = defaultdict(lambda: False)
totalValue = {}

for row in data:
    row = row.split(" -> ")
    name, weight = row[0].strip(")").split(" (")
    adjDict[name][0] = int(weight)

    if len(row) == 2:
        for child in row[1].split(", "):
            adjDict[name][1].append(child)
            adjDict[child][2].append(name)
        

def updateWithTotal(cur):
    total = []
    for next in adjDict[cur][1]:
        total.append(updateWithTotal(next))
    totalValue[cur] = sum(total) + adjDict[cur][0]
    validDict[cur] = (not total) or sum(total) % total[0] == 0
    return sum(total) + adjDict[cur][0]


childrenSet = set()
for _, children, _ in adjDict.values():
    childrenSet.update(set(children))
start = (adjDict.keys() ^ childrenSet).pop()
updateWithTotal(start)

for node in adjDict:
    if not validDict[node] and all(validDict[child] for child in adjDict[node][1]):
        correct = mode(totalValue[child] for child in adjDict[node][1])
        for child in adjDict[node][1]:
            if totalValue[child] != correct:
                diff = correct - totalValue[child]
                print(diff + adjDict[child][0])






        
    
