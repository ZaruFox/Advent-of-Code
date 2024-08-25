from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy
from copy import deepcopy

ALLELEMENTS = "PTORCED"

def hash(pos, state):
    hash_ = []
    for element in ALLELEMENTS:
        hash_.append((findObj(f"{element}M", state), findObj(f"{element}G", state)))

    return (tuple(sorted(hash_)), pos)
    

def checkValid(state):
    for obj in state:
        if obj[1] == "M" and f"{obj[0]}G" not in state and any(x[1] == "G" for x in state):
            return False
    return True

def findPair(obj, state):
    if obj[1] == "M":
        target = f"{obj[0]}G"
    else:
        target = f"{obj[0]}M"

    return findObj(target, state)

def findObj(target, state):
    for i in range(4):
        if target in state[i]:
            return i
        
#, "EG", "EM", "DG", "DM"
queue = deque([(0, 0, [{"PG", "TG", "TM", "OG", "RG", "RM", "CG", "CM", "EG", "EM", "DG", "DM"}, {"PM", "OM"}, set(), set()])])
visited = set()

while queue:
    cost, pos, state = queue.popleft()
    
    hashedState = hash(pos, state)
    if hashedState in visited:
        continue
    visited.add(hashedState)

    if (not state[0]) and (not state[1]) and (not state[2]):
        print(cost)
        break

    stateList = [list(x) for x in state]
    visitedObjState = set()

    for i in range(len(state[pos])):
        curObj = stateList[pos][i]

        objState = (findPair(curObj, state), curObj[1])
        if objState in visitedObjState:
            continue
        visitedObjState.add(objState)

        for nextLevel in range(max(pos-1, 0), min(pos+2, 4)):
            if nextLevel == pos:
                continue

            if checkValid(state[nextLevel] | {curObj}) and checkValid(state[pos] ^ {curObj}):
                newState = deepcopy(state)
                newState[nextLevel] = state[nextLevel] | {curObj}
                newState[pos] = state[pos] ^ {curObj}

                queue.append((cost+1, nextLevel, newState))

        for j in range(i+1, len(state[pos])):

            for nextLevel in range(max(pos-1, 0), min(pos+2, 4)):
                if nextLevel == pos:
                    continue

                if checkValid(state[nextLevel] | {curObj, stateList[pos][j]}) and checkValid(state[pos] ^ {curObj, stateList[pos][j]}):
                    newState = deepcopy(state)
                    newState[nextLevel] = state[nextLevel] | {curObj, stateList[pos][j]}
                    newState[pos] = state[pos] ^ {curObj, stateList[pos][j]}

                    queue.append((cost+1, nextLevel, newState))