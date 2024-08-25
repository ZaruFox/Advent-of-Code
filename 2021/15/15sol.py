from collections import deque


def getAdjacentPos(x, y, heightmap):
    res = []
    if x != 0:
        res.append((x - 1, y))

    if y != 0:
        res.append((x, y - 1))

    if x != len(heightmap[0]) - 1:
        res.append((x + 1, y))

    if y != len(heightmap) - 1:
        res.append((x, y + 1))

    return res


class Graph:

    def __init__(self, nodes, relations):
        self.graph = {}

        for node in nodes:
            self.graph[node] = []

        for node1, node2, distance in relations:
            self.graph[node1].append([node2, distance])

    def getAdj(self, node):
        return self.graph[node]


def dijkstra(graph, startPos):
    shortestPath = {startPos: 0}
    queue = deque([startPos])

    while queue:
        curNode = queue.popleft()

        for adj, distance in graph.getAdj(curNode):
            if not adj in shortestPath.keys(
            ) or shortestPath[adj] > distance + shortestPath[curNode]:
                shortestPath[adj] = distance + shortestPath[curNode]
                queue.append(adj)

    return shortestPath


data = []
nodes = []
relations = []

with open("15data.txt") as f:
    for line in f:
        data.append([int(x) for x in list(line.strip())])

for y in range(len(data)):
    for x in range(len(data[0])):
        nodes.append((x, y))

for node in nodes:
    for adjNode in getAdjacentPos(node[0], node[1], data):
        relations.append([node, adjNode, data[adjNode[1]][adjNode[0]]])

graph = Graph(nodes, relations)

print(dijkstra(graph, (0, 0))[(len(data[0]) - 1, len(data) - 1)])

# part 2

data = []
nodes = []
relations = []
for i in range(5):
    with open("15data.txt") as f:
        for line in f:
            temp = []
            for j in range(5):
                for num in [int(x) + i + j for x in list(line.strip())]:
                    while num > 9:
                        num -= 9

                    temp.append(num)
            data.append(temp)

for y in range(len(data)):
    for x in range(len(data[0])):
        nodes.append((x, y))

for node in nodes:
    for adjNode in getAdjacentPos(node[0], node[1], data):
        relations.append([node, adjNode, data[adjNode[1]][adjNode[0]]])

graph = Graph(nodes, relations)

print(dijkstra(graph, (0, 0))[(len(data[0]) - 1, len(data) - 1)])
