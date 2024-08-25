from collections import deque

class Flipflop:
    def __init__(self, destinations):
        self.destinations = destinations
        self.state = False

    def pulse(self, senderName, pulseType):
        if pulseType:
            return None

        self.state = not self.state
        return self.state
            
        

class Conjunction:
    def __init__(self, destinations):
        self.destinations = destinations
        self.inputStates = {}

    def pulse(self, senderName, pulseType):
        self.inputStates[senderName] = pulseType
        return not all(self.inputStates.values())


startNodes = []
vertexDict = {}
SYMBOLTOCLASS = {"%":Flipflop, "&":Conjunction}

# read file and generate all nodes
with open("data.txt") as f:
    for line in f:
        name, destinations = line.strip().split(" -> ")
        destinations = destinations.split(", ")

        if name == "broadcaster":
            startNodes = destinations
        else:
            vertexDict[name[1:]] = SYMBOLTOCLASS[name[0]](destinations)

# find all the inputs to Conjunction nodes
for name, node in vertexDict.items():
    for nextName in node.destinations:
        if nextName in vertexDict and type(vertexDict[nextName]) == Conjunction:
            vertexDict[nextName].inputStates[name] = False

# main loop
counter = {False: 1000, True: 0}
for _ in range(1000):
    queue = deque([(name, False, "broadcaster") for name in startNodes])

    while queue:
        curName, pulseType, senderName= queue.popleft()
        
        counter[pulseType] += 1
        if not curName in vertexDict:
            continue
        
        nextPulse = vertexDict[curName].pulse(senderName, pulseType)
        if nextPulse == None:
            continue
            
        for nextName in vertexDict[curName].destinations:
            queue.append((nextName, nextPulse, curName))

        
print(counter[False] * counter[True])