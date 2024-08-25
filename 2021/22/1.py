from itertools import combinations
import re

class Cube:
    def __init__(self, minX, maxX, minY, maxY, minZ, maxZ):
        assert maxX >= minX and maxY >= minY and maxZ >= minZ
        
        self.x = (minX, maxX)
        self.y = (minY, maxY)
        self.z = (minZ, maxZ)

    def isOverlapping(self, other):
        return not (self.x[0] > other.x[1] or self.x[1] < other.x[0] or self.y[0] > other.y[1] or self.y[1] < other.y[0] or self.z[0] > other.z[1] or self.z[1] < other.z[0])

    def findOverlap(self, other):
        if not self.isOverlapping(other):
            return None

        return Cube(max(self.x[0], other.x[0]), min(self.x[1], other.x[1]), max(self.y[0], other.y[0]), min(self.y[1], other.y[1]), max(self.z[0], other.z[0]), min(self.z[1], other.z[1]))

    def getSize(self):
        return (1+self.x[1]-self.x[0]) * (1+self.y[1]-self.y[0]) * (1+self.z[1]-self.z[0])

with open("data.txt") as f:
    data = [line.strip() for line in f]

cubes = []
for row in data:
    type, position = row.split()

    newCube = Cube(*[int(x) for x in re.split(r"\.\.|,y=|,z=", position.lstrip("x="))])

    if newCube.x[0] > 50 or newCube.x[0] < -50:
        continue

    for oldCube, parity in cubes.copy():
        if (tmp := oldCube.findOverlap(newCube)) != None:
            cubes.append((tmp, -parity))

    if type == "on":
        cubes.append((newCube, 1))

totalSize = 0
print(len(cubes))
for cube, parity in cubes:
    totalSize += cube.getSize() * parity
print(totalSize)