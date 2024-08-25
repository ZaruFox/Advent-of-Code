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

total0=bfs([startingPoint], 13000000, 0)
total1=bfs([startingPoint], 13000000, 1)

l = (0, 65)
r = (130, 65)
d = (65, 130)
u = (65, 0)

l1=bfs([l], 130, 0)
r1=bfs([r], 130, 0)
u1=bfs([u], 130, 0)
d1=bfs([d], 130, 0)

ul1=bfs([u, l], 130, 0)
dr1=bfs([d, r], 130, 0)
ur1=bfs([u, r], 130, 0)
dl1=bfs([d, l], 130, 0)

a = bfs([(0,0)], 65, 0)
b = bfs([(130,0)], 65, 0)
c = bfs([(0,130)], 65, 0)
d = bfs([(130,130)], 65, 0)
print(202300*(a+b+c+d) + l1+r1+u1+d1+ 202299*(ul1+dr1+ur1+dl1) + 4*(total1)*(202298/4*(2+202298)) + 4*(total0)*((202298/2+1)/2*(1+202299)) + total1)