from collections import deque

VALIDMOVES = {"|": [(0, -1), (0, 1)], "-": [(-1, 0), (1, 0)],
     "F": [(0, 1), (1, 0)], "L": [(0, -1), (1, 0)],
     "J": [(0, -1), (-1, 0)], "7": [(0, 1), (-1, 0)]}
DIRECTIONS = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}
# J,F SWAP PLACE
# L,7 SWAP PLACE AND NEGATIVE

map = []
with open("data.txt") as f:
    y = 0
    for line in f:
        if "S" in line:
            start = (line.find("S"), y)
            line = line.replace("S", "|")
        map.append(list(line.strip()))
        y += 1        

path = set()
cur = start
prev = None
while True:
    for diff in VALIDMOVES[map[cur[1]][cur[0]]]:
        next = (diff[0] + cur[0], diff[1] + cur[1])
        if next == prev:
            continue
        prev, cur = cur, next
        break

    path.add(cur)
    if cur == start:
        break

#bfs
stack = deque([(0, 0, None)])
visited = set()
while stack:
    cur = stack.popleft()

    if cur in visited:
        continue
    visited.add(cur)


    x, y, side = cur

    if (x, y) in path:
        validDirections = set(VALIDMOVES[map[y][x]])
        if not side in validDirections:
            validDirections.add(side)
            validDirections.discard((-side[0], -side[1]))
        else:
            validDirections.discard((side[0], side[1]))

    else:
        validDirections = set([(0,1),(0,-1),(1,0),(-1,0)])


    for newDirection in validDirections:
        nextX, nextY = x+newDirection[0], y+newDirection[1]
        if nextX < 0 or nextX >= len(map[0]) or nextY < 0 or nextY >= len(map):
            continue

        if (x, y) in path and newDirection in VALIDMOVES[map[y][x]]:
            nextSide = side
        else:
            nextSide = (-newDirection[0], -newDirection[1])

        stack.append((nextX, nextY, nextSide))
        if map[nextY][nextX] in ("J", "F"):
            stack.append((nextX, nextY, (nextSide[1], nextSide[0])))
        elif map[nextY][nextX] in ("7", "L"):
            stack.append((nextX, nextY, (-nextSide[1], -nextSide[0])))

print(len(map)*len(map[0]) - len(set([(x,y) for x,y,_ in visited])))