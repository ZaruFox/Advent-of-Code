def calcDist(coords1, coords2, expandedLines):
    additionalDist = 0
    for x in expandedLines["x"]:
        if min(coords1[0], coords2[0]) < x < max(coords1[0], coords2[0]):
            additionalDist += 999999

    for y in expandedLines["y"]:
        if min(coords1[1], coords2[1]) < y < max(coords1[1], coords2[1]):
            additionalDist += 999999
            
    return abs(coords1[0]-coords2[0])+abs(coords1[1]-coords2[1]) + additionalDist

map = []
expandedLines = {"x": [], "y": []}
with open("data.txt") as f:
    y = 0
    for line in f:
        row = list(line.strip())
        if not "#" in row:
            expandedLines["y"].append(y)
        map.append(row)
        y += 1

x = 0
while x < len(map[0]):
    if not "#" in [row[x] for row in map]:
        expandedLines["x"].append(x)
    x += 1


galaxyLocations = []
result = 0
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == "#":
            result += sum([calcDist((x,y), coords2, expandedLines) for coords2 in galaxyLocations])
            galaxyLocations.append((x,y))

print(result)