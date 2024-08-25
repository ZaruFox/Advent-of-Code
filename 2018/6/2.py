from collections import deque, defaultdict
import math

origins = []
with open("data.txt") as f:
    for line in f:
        origins.append(tuple([int(x) for x in line.strip().split(",")]))

minX = min([x[0] for x in origins])-5
minY  = min([x[1] for x in origins])-5
maxX = max([x[0] for x in origins])+5
maxY = max([x[1] for x in origins])+5

totalCost = defaultdict(int)
queue = deque([origins[i] + (i,0) for i in range(len(origins))])
visited = defaultdict(set)

for i, origin in enumerate(origins):
    visited[origin].add(i)

while queue:
    x, y, originIndex, cost = queue.popleft()
    
    if not (minX <= x <= maxX and minY <= y <= maxY):
        continue

    totalCost[(x, y)] += cost

    for newX, newY in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
        if originIndex in visited[(newX , newY)]:
            continue
        visited[(newX, newY)].add(originIndex)

        queue.append((newX, newY, originIndex, cost+1))

print(len([x for x in totalCost if totalCost[x] < 10000]))