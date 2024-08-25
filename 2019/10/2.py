from collections import defaultdict
import math
locations = []

with open("data.txt") as f:
    y = 0
    for line in f:
        for x in range(len(line.strip())):
            if line[x] == "#":
                locations.append((x, y))
        y -= 1

visibleDict = defaultdict(list)
for i in range(len(locations)):
    for j in range(i+1, len(locations)):
        minY = min(locations[i][1], locations[j][1])
        maxY = max(locations[i][1], locations[j][1])
        minX = min(locations[i][0], locations[j][0])
        maxX = max(locations[i][0], locations[j][0])

        if locations[i][0] == locations[j][0]:
            isVisible = not any((locations[j][0], y) in locations for y in range(minY+1, maxY))
            m = math.inf
            
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
            visibleDict[locations[i]].append((locations[j], m))
            visibleDict[locations[j]].append((locations[i], m))


targetAstroid = None
for key in visibleDict:
    if targetAstroid == None or len(visibleDict[targetAstroid]) < len(visibleDict[key]):
        targetAstroid = key

rightAstroids = []
leftAstroids = []
topAstroid = ()
bottomAstroid = ()

for coords, gradient in visibleDict[targetAstroid]:
    if coords[0] > targetAstroid[0]:
        rightAstroids.append((coords, gradient))
    elif coords[0] < targetAstroid[0]:
        leftAstroids.append((coords, gradient))
    elif coords[1] > targetAstroid[0]:
        topAstroid = (coords, gradient)
    else:
        bottomAstroid = (coords, gradient)

finalOrder = [topAstroid] + sorted(rightAstroids, key = lambda x: x[1], reverse = False) + [bottomAstroid] + sorted(leftAstroids, key = lambda x: x[1], reverse = True)
print(finalOrder[199][0]*100 - finalOrder[199][1])