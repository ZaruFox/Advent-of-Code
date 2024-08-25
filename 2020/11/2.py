from copy import deepcopy

def getAdj(x, y):
    return [(x-1,y-1),(x-1, y), (x-1,y+1), (x,y-1), (x,y+1), (x+1,y-1), (x+1,y), (x+1,y+1)]

data = []
with open("data.txt") as f:
    for line in f:
        data.append(list(line.strip()))

while True:
    #print("\n".join(["".join(x) for x in data]), "\n")
    original = deepcopy(data)
    changed = False

    for y in range(len(data)):
        for x in range(len(data[0])):
            allAdjacent = []
            for deltaX, deltaY in getAdj(0, 0):
                newX, newY = x + deltaX, y + deltaY
                while 0 <= newX < len(data[0]) and 0 <= newY < len(data):
                    if original[newY][newX] in "L#":
                        allAdjacent.append(original[newY][newX])
                        break
                    newX += deltaX
                    newY += deltaY
                    
            if "#" not in allAdjacent and original[y][x] == "L":
                data[y][x] = "#"
                changed = True
            elif allAdjacent.count("#") >= 5 and original[y][x] == "#":
                data[y][x] = "L"
                changed = True

    if not changed:
        break

print(sum([data[i].count("#") for i in range(len(data))]))