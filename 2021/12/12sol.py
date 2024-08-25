from collections import deque
class Graph:
    def __init__(self, nodes, relations):
        self.graph = {}

        for node in nodes:
            self.graph[node] = []

        for node1, node2 in relations:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

    def getAdj(self, node):
        return self.graph[node]

relations = []
nodes = set()
with open("12data.txt") as f:
    for line in f:
        data = line.strip().split("-")
        relations.append(data)
        nodes.add(data[0])
        nodes.add(data[1])

caveMap = Graph(nodes, relations)
queue = deque([ [("start",), False] ])
x = set()

while queue:
    temp = queue.popleft()
    curPath, repeated = temp[0], temp[1]
    if curPath[-1] == "end":
        x.add(curPath)
        continue
        
    for cave in caveMap.getAdj(curPath[-1]):
        if cave == "start":
            continue

        temp = cave in curPath
        if cave.isupper() or not temp:
            queue.append([curPath + (cave,), repeated])

        #part 2   
        if temp and not repeated:
            queue.append([curPath + (cave,), True])
            
        

print(len(x))
