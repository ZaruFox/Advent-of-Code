import re
import math

class Point:
    def __init__(self, x, y, xDelta, yDelta) -> None:
        self.x = x
        self.y = y
        self.xDelta = xDelta
        self.yDelta = yDelta

    def update(self):
        self.x += self.xDelta
        self.y += self.yDelta

        return(self.x, self.y)

points = []
with open("data.txt") as f:
    for line in f:
        points.append(Point(*[int(x) for x in re.split(r", *|> velocity=< *", line.strip("position=< >\n"))]))

spread = math.inf
pointPositions = []
time = 0
while True:
    minX = minY = math.inf
    maxX = maxY = -math.inf

    newPositions = []
    for point in points:
        x, y = point.update()

        newPositions.append((x, y))
        minX, minY, maxX, maxY = min(minX, x), min(minY, y), max(maxX, x), max(maxY, y)

    newSpread = (maxX-minX) * (maxY-minY)
    if newSpread > spread:
        print(time)
        break
    
    pointPositions = newPositions
    spread = newSpread
    time += 1