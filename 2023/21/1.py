from collections import deque

graph = []
startingPoint = ()

with open("data.txt") as f:
    y = 0
    for line in f:
        if "S" in line:
            startingPoint = (line.find("S"), y)
            line.replace("S", ".")
            
        graph.append(line.strip())
        y += 1

queue = deque([(startingPoint, 0)])
visited = {startingPoint: 0}

while queue:
    coordinates, steps = queue.popleft()
    x, y = coordinates

    if steps >= 64:
        continue

    for newX, newY in [(x-1, y), (x,y-1), (x,y+1), (x+1,y)]:
        if not (0 <= newX < len(graph[0]) and 0 <= newY < len(graph)):
            continue

        if (newX, newY) in visited:
            continue

        if graph[newY][newX] == "#":
            continue
            
        visited[(newX, newY)] = steps + 1
        queue.append(((newX, newY), steps + 1))

print(len([x for x in visited.values() if x % 2 == 0]))