from collections import deque
from functools import cache
import heapq
import math

map = []
with open("data.txt") as f:
    for line in f:
        map.append(line.strip())

adjGraph = [set()]
coordsToNodeIndex = {(1, 0): 0}
stack = deque([(1, 0, 0, None)])
visited = set()

while stack:
    x, y, prevNode, prevMove = stack.popleft()
    
    if (x, y) in visited:
        continue
    visited.add((x, y))

    stepsTaken = 0
    while True:
        if x == len(map[0]) - 2 and y == len(map) - 1:
            adjGraph[prevNode].add((-1, stepsTaken))
            break
        
        validMoves = []
        for nextMove in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
            if nextMove == prevMove or map[nextMove[1]][nextMove[0]] == "#":
                continue
            validMoves.append(nextMove)

        if len(validMoves) == 1:
            prevMove = (x, y)
            x, y = validMoves[0]
            stepsTaken += 1
            
        elif len(validMoves) != 0:
            if (x, y) in coordsToNodeIndex:
                newNode = coordsToNodeIndex[(x, y)]
                adjGraph[prevNode].add((newNode, stepsTaken))
                adjGraph[newNode].add((prevNode, stepsTaken))

            else:
                newNode = len(adjGraph)
                coordsToNodeIndex[(x, y)] = newNode
                adjGraph[prevNode].add((newNode, stepsTaken))
                adjGraph.append({(prevNode, stepsTaken)})
            
                for move in validMoves:
                    stack.append((move[0], move[1], newNode, (x, y)))
            break
            
        else:
            break
                

# dfs
stack = deque([(0, 0, set())])
res = 0
while stack:
    node, totalCost, visited = stack.pop()

    for nextNode, cost in adjGraph[node]:
        if nextNode in visited:
            continue

        if nextNode == -1:
            res = max(res, totalCost + cost + len(visited))
            continue

        stack.append((nextNode, totalCost+cost, visited | {node}))

print(res)
        
    