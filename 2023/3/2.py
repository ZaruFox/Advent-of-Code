import math
from collections import defaultdict 

def checkForGears(data, x, y):
    adjGears = set()
    for x2, y2 in [(x-1,y-1),(x-1, y), (x-1,y+1), 
                   (x,y-1), (x,y+1), 
                   (x+1,y-1), (x+1,y), (x+1,y+1)]:
        if data[y2][x2] == "*":
            adjGears.add((x2, y2))
    return adjGears

data = []
with open("data.txt") as f:
    for line in f:
        data.append("." + line.strip() + ".")
data.insert(0, "."*len(data[0]))
data.append("."*len(data[0]))

gears = defaultdict(list)
for y in range(len(data)):
    x = 0
    while x < len(data):
        adjGears = set()
        if data[y][x].isdigit():
            number = ""
            while data[y][x].isdigit():
                number += data[y][x]
                adjGears.update(checkForGears(data, x, y))
                x += 1

            for gear in adjGears:
                gears[gear].append(int(number))
        x += 1

totalGearRatio = 0
for adjNumbers in gears.values():
    if len(adjNumbers) == 2:
        totalGearRatio += math.prod(adjNumbers)
print(totalGearRatio)