from collections import defaultdict

bricks = []

with open("data.txt") as f:
    for line in f:
        bricks.append([[int(x) for x in coordinate.split(",")] for coordinate in line.strip().split("~")])

bricks.sort(key = lambda x:min(x[0][2], x[1][2]))
bricksCoordinates = {}
bricksOnTop = [[] for i in range(len(bricks))]
bricksBelow = [[] for i in range(len(bricks))]

for i, brick in enumerate(bricks):
    newZ = 0
    bricksSupporting = set()
    for x in range(brick[0][0], brick[1][0]+1):
        for y in range(brick[0][1], brick[1][1]+1):
            if not (x, y) in bricksCoordinates:
                continue

            if bricksCoordinates[(x, y)][0] > newZ:
                bricksSupporting = set([bricksCoordinates[(x, y)][1]])
                newZ = bricksCoordinates[(x, y)][0]
            elif bricksCoordinates[(x, y)][0] == newZ:
                bricksSupporting.add(bricksCoordinates[(x, y)][1])

    for x in range(brick[0][0], brick[1][0]+1):
        for y in range(brick[0][1], brick[1][1]+1):
            bricksCoordinates[(x, y)] = (newZ+abs(brick[0][2]-brick[1][2])+1, i)

    for support in bricksSupporting:
        bricksOnTop[support].append(i)
    bricksBelow[i] = bricksSupporting

res = 0
for i in range(len(bricks)):
    valid = True
    for j in bricksOnTop[i]:
        if len(bricksBelow[j]) < 2:
            valid = False
            break
            
    if valid:
        res += 1

print(res)