tiles = {}

with open("data.txt") as f:
    leftBorder = []
    rightBorder = []
    topBorder = ""
    bottomBorder = ""
    for line in f:
        if line.startswith("Tile"):
            tileNumber = int(line.lstrip("Tile ").rstrip(":\n"))
        elif line == "\n":
            tiles[tileNumber] = ("".join(leftBorder), "".join(rightBorder), topBorder, bottomBorder)
            leftBorder = []
            rightBorder = []
            topBorder = ""
            bottomBorder = ""
        else:
            if topBorder == "":
                topBorder = line.strip()
            bottomBorder = line.strip()
            leftBorder.append(line[0])
            rightBorder.append(line[-2])
    tiles[tileNumber] = ("".join(leftBorder), "".join(rightBorder), topBorder, bottomBorder)

tmp = []
for val in tiles.values():
    tmp += val

borderCount = {}
for border in tmp:
    if border in borderCount:
        borderCount[border] += 1
    elif border[::-1] in borderCount:
        borderCount[border[::-1]] += 1
    else:
        borderCount[border] = 1
        

res = 1
for key in tiles:
    connections = 0
    for border in tiles[key]:
        if (border in borderCount and borderCount[border] == 2) or (border[::-1] in borderCount and borderCount[border[::-1]] == 2):
            connections += 1
        
    if connections == 2:
        res *= key
print(res)