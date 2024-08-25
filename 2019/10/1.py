from collections import defaultdict
import math
locations = []

with open("data.txt") as f:
    y = 0
    for line in f:
        for x in range(len(line.strip())):
            if line[x] == "#":
                locations.append((x, y))
        y += 1

visibleDict = defaultdict(list)
for i in range(len(locations)):
    for j in range(i+1, len(locations)):
        minY = min(locations[i][1], locations[j][1])
        maxY = max(locations[i][1], locations[j][1])
        minX = min(locations[i][0], locations[j][0])
        maxX = max(locations[i][0], locations[j][0])
        
        if locations[i][0] == locations[j][0]:
            isVisible = not any((locations[j][0], y) in locations for y in range(minY+1, maxY))
        else:
            m = (locations[i][1]-locations[j][1])/(locations[i][0]-locations[j][0])
            c = locations[i][1] - m * locations[i][0]
    
            isVisible = True
            for astroid in locations:
                if astroid == locations[i] or astroid == locations[j]:
                    continue

                if not (minX <= astroid[0] <= maxX and minY <= astroid[1] <= maxY):
                    continue

                if math.isclose(astroid[1], m*astroid[0] + c):
                    isVisible = False
                    break
                
        if isVisible:
            visibleDict[locations[i]].append(locations[j])
            visibleDict[locations[j]].append(locations[i])


print(max([len(x) for x in visibleDict.values()]))