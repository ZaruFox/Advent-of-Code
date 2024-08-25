from collections import deque
from math import inf

with open("data.txt") as f:
    data = f.read().splitlines()

minY = inf
maxY = -inf
walls = set()
for row in data:
    firstCoord, secondCoord = row.split(", ")
    if row[0] == "x":
        x = int(firstCoord.strip("x="))
        y1, y2 = [int(z) for z in secondCoord.strip("y=").split("..")]
        for y in range(y1, y2+1):
            walls.add((x, y))
        maxY = max(maxY, y)
        minY = min(minY, y1)

    else:
        y = int(firstCoord.strip("y="))
        maxY = max(maxY, y)
        minY = min(minY, y)
        x1, x2 = [int(z) for z in secondCoord.strip("x=").split("..")]

        for x in range(x1, x2+1):
            walls.add((x, y))


waterQueue = deque([(500, minY)])
visited = set()
fallingWater = set()
restingWater = set()

while waterQueue:
    waterX, waterY = waterQueue.popleft()
    tmpStack = deque()
    expand = False

    while True:
        if (waterX, waterY) in walls or (waterX, waterY) in restingWater:
            expand = True
            break

        if (waterX, waterY) in fallingWater or waterY > maxY:
            break

        tmpStack.append((waterX, waterY))
        waterY += 1

    if expand:
        while True:
            if tmpStack:
                restingX, restingY = tmpStack.pop()
            else:
                restingY -= 1
                
            if (restingX, restingY+1) in fallingWater:
                break

            water = {(restingX, restingY)}
            resting = True

            x = restingX - 1
            while True:
                if (x, restingY) in walls:
                    break

                if not ((x, restingY+1) in walls or (x, restingY+1) in restingWater):
                    if (x, restingY) in visited:
                        break
                    visited.add((x, restingY))
                    waterQueue.append((x, restingY))
                    resting = False
                    break

                water.add((x, restingY))
                x -= 1

            x = restingX + 1
            while True:
                if (x, restingY) in walls:
                    break

                if not ((x, restingY+1) in walls or (x, restingY+1) in restingWater):
                    if (x, restingY) in visited:
                        break
                    visited.add((x, restingY))
                    waterQueue.append((x, restingY))
                    resting = False
                    break

                water.add((x, restingY))
                x += 1

            if resting:
                restingWater.update(water)
                fallingWater -= water
            else:
                fallingWater.update(water)
                break

    fallingWater.update(tmpStack)

print(len(fallingWater | restingWater))
