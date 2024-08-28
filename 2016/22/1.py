from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

class Node:
    def __init__(self, x, y, size, used, avail, usePercent):
        self.x = x
        self.y = y 
        self.size = size
        self.used = used
        self.avail = avail
        self.usePercent = usePercent

    def __repr__(self):
        return f"Node at ({self.x}, {self.y}) with available space of {self.avail} and used space of {self.used}\n"

nodes = []
with open("data.txt") as f:
    for line in f:
        # get all integer values
        nodeData = re.split("/dev/grid/node-x|-y|T? +|%\n?", line)

        # convert all values to int and removes empty strings
        nodeData = [int(x) for x in nodeData if x]

        nodes.append(Node(*nodeData))

viableNodes = 0
for a in range(len(nodes)):
    for b in range(len(nodes)):
        if nodes[a].used != 0 and a != b and nodes[a].used <= nodes[b].avail:
            viableNodes += 1


print(viableNodes)