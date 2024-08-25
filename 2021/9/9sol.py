from collections import deque

def viewAdjacent(x, y, heightmap):
    res = []
    if x != 0:
        res.append(heightmap[y][x-1])

    if y != 0:
        res.append(heightmap[y-1][x])

    if x != len(heightmap[0]) - 1:
        res.append(heightmap[y][x+1])

    if y != len(heightmap) - 1:
        res.append(heightmap[y+1][x])

    return res

def getAdjacentIndex(x, y, heightmap):
    res = []
    if x != 0:
        res.append([x-1, y])

    if y != 0:
        res.append([x, y-1])

    if x != len(heightmap[0]) - 1:
        res.append([x+1, y])

    if y != len(heightmap) - 1:
        res.append([x, y+1])

    return res
        
heightmap = []
lowPoints = []
res = 0
with open("9data.txt") as f:
    for line in f:
        heightmap.append([int(x) for x in list(line.strip())])

for y in range(len(heightmap)):
    for x in range(len(heightmap[0])):
        lowPoint = True
        for adjHeight in viewAdjacent(x, y, heightmap):
            lowPoint = lowPoint and adjHeight > heightmap[y][x]

        if lowPoint:
            lowPoints.append([x,y])
            res += 1 + heightmap[y][x]
        
print("ans1: ", res)

# part 2

def bfs(startPos, heightmap):
    size = 0
    queue = deque([startPos])
    visited = set()

    while queue:
        curPos = queue.popleft()
        size += 1
        visited.add(tuple(curPos))
        
        for adjPos in getAdjacentIndex(curPos[0], curPos[1], heightmap):
            if heightmap[adjPos[1]][adjPos[0]] != 9 and (not ((adjPos[0], adjPos[1]) in visited) and not [adjPos[0], adjPos[1]] in queue):
                queue.append(adjPos)
                
    return size

sizes = []
for i, pos in enumerate(lowPoints):
    sizes.append(bfs(pos, heightmap))

res = 1
for size in sorted(sizes)[-3:]:
    res *= size
print(res)

            
