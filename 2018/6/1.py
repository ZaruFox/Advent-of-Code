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

area = {i:0 for i in range(len(origins))}
queue = deque([origins[i] + (i,0) for i in range(len(origins))])
visited = {x: [set(), 0] for x in origins}
claimed = set()

while queue:
    x, y, originIndex, cost = queue.popleft()

    if len(visited[(x, y)][0]) > 1 or (x, y) in claimed:
        continue
    claimed.add((x, y))
    
    if not (minX <= x <= maxX and minY <= y <= maxY):
        area[originIndex] = -math.inf
        continue

    area[originIndex] += 1

    for newX, newY in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
        if (newX, newY) not in visited:
            visited[(newX, newY)] = [{originIndex}, cost+1]
        elif cost+1 == visited[(newX, newY)][1]:
            visited[(newX, newY)][0].add(originIndex)
            continue
        else:
            continue
            
        queue.append((newX, newY, originIndex, cost+1))

print(area)
print(max(area.values()))
