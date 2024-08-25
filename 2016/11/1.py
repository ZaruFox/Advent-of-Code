from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy
from copy import deepcopy

def hash(pos, state):
    return tuple([tuple(sorted(x)) for x in state] + [pos])

def checkValid(state):
    for obj in state:
        if obj[1] == "M" and f"{obj[0]}G" not in state and any(x[1] == "G" for x in state):
            return False
    return True
        

queue = deque([(0, 0, [{"PG", "TG", "TM", "OG", "RG", "RM", "CG", "CM"}, {"PM", "OM"}, set(), set()])])
visited = set()

while queue:
    cost, pos, state= queue.popleft()
    
    hashedState = hash(pos, state)
    if hashedState in visited:
        continue
    visited.add(hashedState)

    if (not state[0]) and (not state[1]) and (not state[2]):
        print(cost)
        break

    stateList = [list(x) for x in state]
    for i in range(len(state[pos])):

        for nextLevel in range(max(pos-1, 0), min(pos+2, 4)):
            if nextLevel == pos:
                continue

            if checkValid(state[nextLevel] | {stateList[pos][i]}) and checkValid(state[pos] ^ {stateList[pos][i]}):
                newState = deepcopy(state)
                newState[nextLevel] = state[nextLevel] | {stateList[pos][i]}
                newState[pos] = state[pos] ^ {stateList[pos][i]}

                queue.append((cost+1, nextLevel, newState))

        for j in range(i+1, len(state[pos])):

            for nextLevel in range(max(pos-1, 0), min(pos+2, 4)):
                if nextLevel == pos:
                    continue

                if checkValid(state[nextLevel] | {stateList[pos][i], stateList[pos][j]}) and checkValid(state[pos] ^ {stateList[pos][i], stateList[pos][j]}):
                    newState = deepcopy(state)
                    newState[nextLevel] = state[nextLevel] | {stateList[pos][i], stateList[pos][j]}
                    newState[pos] = state[pos] ^ {stateList[pos][i], stateList[pos][j]}

                    queue.append((cost+1, nextLevel, newState))

        

            



