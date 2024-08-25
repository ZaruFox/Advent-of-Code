from collections import deque

              # up       right   down    left
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
layout = []

with open("data.txt") as f:
    for row in f:
        layout.append(row.strip())

def findEnergized(x, y, direction):
    queue = deque([(x, y, direction)])
    visited = set()
    visitedDirections = set()
    
    while queue:
        x, y, direction = queue.popleft()
    
        while True:
            if not (0 <= x < len(layout[0]) and 0 <= y < len(layout)):
                break
    
            if (x, y, direction) in visitedDirections:
                break
            visitedDirections.add((x, y, direction))
            visited.add((x, y))
    
            if (layout[y][x] == "\\" and direction in (3, 1)) or (layout[y][x] == "/" and direction in (0, 2)):
                direction += 1
                direction %= 4
            elif (layout[y][x] == "\\" and direction in (2, 0)) or (layout[y][x] == "/" and direction in (3, 1)):
                direction -= 1
                direction %= 4
            elif layout[y][x] == "-" and direction in (0, 2):
                queue.append((x-1, y, 3))
                queue.append((x+1, y, 1))
                break
            elif layout[y][x] == "|" and direction in (1, 3):
                queue.append((x, y-1, 0))
                queue.append((x, y+1, 2))
                break
    
    
            x, y = x + DIRECTIONS[direction][0], y + DIRECTIONS[direction][1]
    
    return len(visited)



print(max([findEnergized(x, 0, 2) for x in range(len(layout[0]))] + [findEnergized(x, len(layout)-1, 0) for x in range(len(layout[0]))] + [findEnergized(0, y, 1) for y in range(len(layout))] + [findEnergized(len(layout[0])-1, y, 3) for y in range(len(layout))]))