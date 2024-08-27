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

def bfs(startingPoints, totalSteps=1000000, parity = 0):
    queue = deque([])
    visited = {}
    for point in startingPoints:
        queue.append((point, 0))
        visited[point] = 0
    
    while queue:
        coordinates, steps = queue.popleft()
        x, y = coordinates
    
        if steps >= totalSteps:
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
    return len([x for x in visited.values() if x % 2 == parity])

filled0 = bfs([startingPoint])
filled1 = bfs([startingPoint], parity=1)

dirs = [(0, 65) #l
    , (130, 65) #r
    , (65, 130) #d
    , (65, 0)] #u

corners = sum(bfs([x], 130) for x in dirs) 
innerSides = sum(bfs(x, 130) for x in ([dirs[3], dirs[0]], [dirs[2], dirs[1]], [dirs[3], dirs[1]], [dirs[2], dirs[0]]))
outerSides = sum(bfs([x], 65) for x in [(0, 0), (130, 0), (0, 130), (130, 130)])

length = 202300
print(length*outerSides + (length-1)*innerSides + (length**2 - 2*length + 1)*filled1 + (length**2)*filled0 + corners)