from copy import deepcopy
from collections import Counter

OPPOSITEBORDER = {0:1, 1:0, 2:3, 3:2}

configurations = {}
# find all configurations
for i, base in enumerate([
    [(0, False),(1, False),(2,False),(3,False)], 
    [(3,False),(2,False),(0,True),(1,True)], 
    [(1,True),(0,True),(3,True),(2,True)], 
    [(2,True),(3,True),(1,False),(0,False)]]): 
    configurations[tuple(base)] = (i, False)

    tmp = deepcopy(base)
    tmp[0], tmp[1] = tmp[1], tmp[0]
    for j in (2,3):
        tmp[j] = (tmp[j][0], not tmp[j][1])
    configurations[tuple(tmp)] = (i, True)
    
tiles = {}
tilesFull = {}
with open("data.txt") as f:
    leftBorder = []
    rightBorder = []
    topBorder = ""
    bottomBorder = ""
    for line in f:
        if line.startswith("Tile"):
            tileNumber = int(line.lstrip("Tile ").rstrip(":\n"))
            tilesFull[tileNumber] = []
        elif line == "\n":
            tiles[tileNumber] = ("".join(leftBorder), "".join(rightBorder), topBorder, bottomBorder)
            leftBorder = []
            rightBorder = []
            topBorder = ""
            bottomBorder = ""
        else:
            tilesFull[tileNumber] += [line.strip()]
            if topBorder == "":
                topBorder = line.strip()
            bottomBorder = line.strip()
            leftBorder.append(line[0])
            rightBorder.append(line[-2])
    tiles[tileNumber] = ("".join(leftBorder), "".join(rightBorder), topBorder, bottomBorder)

# group borders
borderToTile = {}
for tile in tiles:
    for border in tiles[tile]:
        if border in borderToTile:
            borderToTile[border] += [tile]
        elif border[::-1] in borderToTile:
            borderToTile[border[::-1]] += [tile]
        else:
            borderToTile[border] = [tile]

# find a corner tile
start = 0
for key in tiles:
    connections = 0
    for border in tiles[key]:
        if (border in borderToTile and len(borderToTile[border]) == 2) or (border[::-1] in borderToTile and len(borderToTile[border[::-1]]) == 2):
            connections += 1

    if connections == 2:
        start = key

class Tile:
    def __init__(self, tileNumber, rotation, xFlip):
        self.tileNumber = tileNumber
        self.rotation = rotation
        self.xFlip = xFlip

    def toFullTile(self):
        tile = tilesFull[self.tileNumber]
        
        for _ in range(self.rotation):
            tile = list(zip(*tile[::-1]))
            
        if self.xFlip:
            tile = [x[::-1] for x in tile]

        return ["".join(x[1:-1]) for x in tile[1:-1]]

def findConnectedTiles(tileNumber):
    res = {}
    for side, border in enumerate(tiles[tileNumber]):
        tmp = border if border in borderToTile else border[::-1]
            
        for connectedTile in borderToTile[tmp]:
            if connectedTile != tileNumber:
                res[side] = (connectedTile, border)
    return res


#    2
# 0     1
#    3
# form grid of tiles
tileGrid = []
nextVerReq = [start, None]
verticalDone = False
while not verticalDone:
    connectedTiles = findConnectedTiles(nextVerReq[0])
    
    for i in connectedTiles:
        if nextVerReq[1] is None:
            break
            
        if connectedTiles[i][1] == nextVerReq[1]:
            topBorder = i
            requiresFlip = False
            connectedTiles.pop(i)
            break
        if connectedTiles[i][1] == nextVerReq[1][::-1]:
            topBorder = i
            requiresFlip = True
            connectedTiles.pop(i)
            break
    

    for config in configurations:
        if len(connectedTiles.keys()) == 1:
            if config[2] == (topBorder, requiresFlip):
                tileGrid.append([Tile(nextVerReq[0], *configurations[config])])
                if not config[1][1]:
                    nextReq = connectedTiles[config[1][0]]
                else:
                    nextReq = (connectedTiles[config[1][0]][0], connectedTiles[config[1][0]][1][::-1])
                verticalDone = True
                break
        else:
            if (tileGrid == [] or config[2] == (topBorder, requiresFlip)):
                tileGrid.append([Tile(nextVerReq[0], *configurations[config])])
                
                if not config[1][1]:
                    nextReq = connectedTiles[config[1][0]]
                else:
                    nextReq = (connectedTiles[config[1][0]][0], connectedTiles[config[1][0]][1][::-1])

                if not config[3][1]:
                    nextVerReq = connectedTiles[config[3][0]]
                else:
                    nextVerReq = (connectedTiles[config[3][0]][0], connectedTiles[config[3][0]][1][::-1])
                break
                    
            
    # complete the horizontal
    horizontalDone = False
    while not horizontalDone:
        connectedTiles = findConnectedTiles(nextReq[0])

        if len(tileGrid) != 1:
            x = tiles[tileGrid[-2][len(tileGrid[-1])].tileNumber]

            for i in connectedTiles:
                if connectedTiles[i][1] in x or connectedTiles[i][1][::-1] in x:
                    connectedTiles.pop(i)
                    break

        for i in connectedTiles:
            if connectedTiles[i][1] == nextReq[1]:
                leftBorder = i
                requiresFlip = False
                connectedTiles.pop(i)
                break
                
            if connectedTiles[i][1] == nextReq[1][::-1]:
                leftBorder = i
                requiresFlip = True
                connectedTiles.pop(i)
                break

        for config in configurations:
            if len(connectedTiles.keys()) == 1-int(verticalDone):
                if config[0] == (leftBorder, requiresFlip):
                    tileGrid[-1].append(Tile(nextReq[0], *configurations[config]))
                    horizontalDone = True
                    break             
            
            else:
                if config[0] == (leftBorder, requiresFlip):
                    tileGrid[-1].append(Tile(nextReq[0], *configurations[config]))
                    if not config[1][1]:
                        nextReq = connectedTiles[config[1][0]]
                    else:
                        nextReq = (connectedTiles[config[1][0]][0], connectedTiles[config[1][0]][1][::-1])
                    break

fullMap = []

for row in tileGrid:
    fullMap += ["" for _ in range(8)]
    for tile in row:
        tmp = tile.toFullTile()
        for i in range(-8,0):
            fullMap[i] += tmp[i+8]

def findMonster(grid):
    res = 0
    monsterCoords = [(0,1),(1,2),(4,2),(5,1),(6,1),(7,2),(10,2),(11,1),(12,1),(13,2),(16,2),(17,1),(18,0),(18,1),(19,1)]
    for y in range(len(grid)-2):
        for x in range(len(grid[0])-19):
            valid = True
            for monsterPart in monsterCoords:
                if grid[monsterPart[1]+y][monsterPart[0]+x] == ".":
                    valid = False
                    break

            if valid:
                res += len(monsterCoords)
    return res

numberOfHash = "".join(fullMap).count("#")
for _ in range(4):
    tmp = findMonster(fullMap) + findMonster([x[::-1] for x in fullMap])
    if tmp != 0:
        print(numberOfHash-tmp)
        break

    fullMap = list(zip(*fullMap[::-1]))


    
        
