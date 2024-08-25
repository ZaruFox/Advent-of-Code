with open("data.txt") as f:
    instructions = [line.strip() for line in f]

litTiles = set()

for directions in instructions:
    i = 0
    x = 0
    y = 0
    while i < len(directions):
        if directions[i:i+2] == "ne":
            y -= 1
            i += 2
            if y % 2 == 0:
                x -= 1
        elif directions[i:i+2] == "se":
            y += 1
            i += 2
            if y % 2 == 0:
                x -= 1
        elif directions[i:i+2] == "nw": 
            x += 1
            y -= 1
            i += 2
            if y % 2 == 0:
                x -= 1
        elif directions[i:i+2] == "sw":
            x += 1
            y += 1
            i += 2
            if y % 2 == 0:
                x -= 1
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

print(len(litTiles))