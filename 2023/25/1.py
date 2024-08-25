from collections import defaultdict, deque

adjList = defaultdict(list)

with open("data.txt") as f:
    for line in f:
        start, destinations = line.strip().split(": ")
        destinations = destinations.split()

        for vertex in destinations:
            adjList[vertex].append(start)
            adjList[start].append(vertex)

edgeVisits = defaultdict(int)

def bfs(start):
    queue = deque([(start, [start])])
    visited = {start: -1}

    while queue:
        vertex, path = queue.popleft()

        for i in range(len(path)-1):
            edgeVisits[(min(path[i], path[i-1]), max(path[i], path[i-1]))] += len(adjList[vertex])
            
        for nextVertex in adjList[vertex]:
            if nextVertex in visited:
                continue
            edgeVisits[(min(vertex, nextVertex), max(vertex, nextVertex))] += 1
            visited[nextVertex] = vertex
            queue.append((nextVertex, path + [nextVertex]))

    return len(visited)

n = len(adjList)
for i, node in enumerate(adjList):
    if i % 50 == 0:
        print(f"{i}/{n}")
    bfs(node)

cutWires = sorted(edgeVisits.items(), key=lambda x: x[1])[-3:]

for edge, _ in cutWires:
    adjList[edge[0]].remove(edge[1])
    adjList[edge[1]].remove(edge[0])

tmp = bfs(list(adjList.keys())[0])
print((n-tmp) * tmp)