from collections import defaultdict

with open("data.txt") as f:
    instructions = [line.strip() for line in f]

litTiles = set()

for directions in instructions:
    i = 0
    x = 0
    y = 0
    while i < len(directions):
        if directions[i:i+2] == "ne":
            if y % 2 == 0:
                x -= 1
            y -= 1
            i += 2
        elif directions[i:i+2] == "se":
            if y % 2 == 0:
                x -= 1
            y += 1
            i += 2
        elif directions[i:i+2] == "nw": 
            if y % 2 == 0:
                x -= 1
            x += 1
            y -= 1
            i += 2
        elif directions[i:i+2] == "sw":
            if y % 2 == 0:
                x -= 1
            x += 1
            y += 1
            i += 2
        elif directions[i] == "e":
            x -= 1
            i += 1
        elif directions[i] == "w":
            x += 1
            i += 1

    if (x, y) in litTiles:
        litTiles.remove((x, y))
    else:
        litTiles.add((x, y))

for _ in range(100):
    adjBlackCount = defaultdict(int)
    for x, y in litTiles:
        if y % 2 == 0:
            adjTiles = ((x-1,y), (x+1,y), (x-1,y-1), (x,y-1), (x-1,y+1), (x,y+1))
        else:
            adjTiles = ((x-1,y), (x+1,y), (x,y-1), (x+1,y-1), (x,y+1), (x+1,y+1))
            
        for adjTile in adjTiles:
            adjBlackCount[adjTile] += 1

    newLitTiles = set()
    for tile, count in adjBlackCount.items():
        if (tile in litTiles and 1 <= count <= 2) or (tile not in litTiles and count == 2):
            newLitTiles.add(tile)
    litTiles = newLitTiles
print(len(litTiles))