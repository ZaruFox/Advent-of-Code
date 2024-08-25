from collections import deque

walls = set()

cur = [0, 0]
with open("data.txt") as f:
    for line in f:
        direction, steps, colour = line.strip().split()

        for i in range(int(steps)):
            if direction == "U":
                cur[1] -= 1
            elif direction == "D":
                cur[1] += 1
            elif direction == "L":
                cur[0] -= 1
            else:
                cur[0] += 1

            walls.add(tuple(cur))


#bfs flood fill
queue = deque([(1, 1)])
visited = set([(1, 1)])

while queue:
    x, y = queue.popleft()

    for xDiff, yDiff in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nextLocation = (x+xDiff, y+yDiff)
        if nextLocation in visited or nextLocation in walls:
            continue
        visited.add(nextLocation)
        queue.append(nextLocation)

print(len(walls) + len(visited))