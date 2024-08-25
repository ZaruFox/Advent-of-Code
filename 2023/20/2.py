from collections import deque, defaultdict
import math

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
counter = 0
cycleDetection = {}
while counter < 4000:

    queue = deque([(name, False, "broadcaster") for name in startNodes])
    counter += 1
    
    while queue:
        curName, pulseType, senderName= queue.popleft()
            
        if not curName in vertexDict:
            continue

        nextPulse = vertexDict[curName].pulse(senderName, pulseType)
        if curName in ("dn", "vm", "kb", "vk") and not nextPulse:
            print(counter, curName)
        if nextPulse == None:
            continue

        for nextName in vertexDict[curName].destinations:
            queue.append((nextName, nextPulse, curName))


print(math.lcm(3769, 3797, 3863, 3931))