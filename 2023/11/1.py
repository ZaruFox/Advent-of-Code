def calcDist(coords1, coords2):
    return abs(coords1[0]-coords2[0])+abs(coords1[1]-coords2[1])

map = []
with open("data.txt") as f:
    for line in f:
        row = list(line.strip())
        if not "#" in row:
            map.append(row)
        map.append(row)

x = 0
while x < len(map[0]):
    if not "#" in [row[x] for row in map]:
        for y in range(len(map)):
            map[y].insert(x, ".")
        x += 1
    x += 1


galaxyLocations = []
result = 0
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == "#":
            result += sum([calcDist((x,y), coords2) for coords2 in galaxyLocations])
            galaxyLocations.append((x,y))

print(result)