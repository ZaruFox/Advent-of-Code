from collections import deque
            # 0 = up, 1 = right, 2 = down, 3 = left
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
VERTICAL = (0, 2)
HORIZONTAL = (1, 3)
layout = []

with open("data.txt") as f:
    for row in f:
        layout.append(row.strip())

queue = deque([(0, 0, 1)])
visitedDirections = set()

while queue:
    x, y, direction = queue.popleft()
    
    while True:
        # check out of index
        if not (0 <= x < len(layout[0]) and 0 <= y < len(layout)):
            break

        # check for looping value
        if (x, y, direction) in visitedDirections:
            break
        visited.add((x, y, direction))

        current = layout[y][x]
        if (current == "\\" and direction in HORIZONTAL) or (current == "/" and direction in VERTICAL):
            direction += 1
            direction %= 4
        elif (current == "\\" and direction in VERTICAL) or (current == "/" and direction in HORIZONTAL):
            direction -= 1
            direction %= 4
        elif current == "-" and direction in VERTICAL:
            queue.append((x-1, y, 3))
            queue.append((x+1, y, 1))
            break
        elif current == "|" and direction in HORIZONTAL:
            queue.append((x, y-1, 0))
            queue.append((x, y+1, 2))
            break
        

        x, y = x + DIRECTIONS[direction][0], y + DIRECTIONS[direction][1]

print(len(set([(x, y) for x, y, _ in visited])))