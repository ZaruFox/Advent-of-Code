from collections import deque
from functools import cache
import math

with open("data2.txt") as f:
    grid = [list(x.strip()) for x in f.readlines()]


keys = set()
positions = []
for y, row in enumerate(grid):
    for x, chara in enumerate(grid[y]):
        if "a" <= chara <= "z":
            keys.add(chara)

        elif chara == "@":
            positions.append((x, y))

@cache
def bfs(x, y, locked):
    visited = {(x, y)}
    queue = deque([(x, y, 0)])
    locked = set(locked)
    res = []

    while queue:
        x, y, cost = queue.popleft()

        for newX, newY in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
            if (newX, newY) in visited or grid[newY][newX] == "#" or grid[newY][newX] in locked:
                continue
            visited.add((newX, newY))

            if "a" <= grid[newY][newX] <= "z" and grid[newY][newX].upper() in locked:
                res.append((newX, newY, cost+1))

            queue.append((newX, newY, cost+1))

    return res

@cache
def dfs(pos, locked):
    if not locked:
        return 0
    
    locked = set(locked)
    pos = list(pos)
    
    res = math.inf
    for i in range(4):
        for newX, newY, cost in bfs(pos[i][0], pos[i][1], tuple(locked)):
            if cost > res:
                break
            tmp, pos[i] = pos[i], (newX, newY)
            res = min(res, cost+dfs(tuple(pos), tuple(locked - {grid[newY][newX].upper()})))
            pos[i] = tmp

    return res


locked = tuple([x.upper() for x in keys])
print(dfs(tuple(positions), locked))