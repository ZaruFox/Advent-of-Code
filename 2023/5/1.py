class Mapping:
    def __init__(self, desti, source, rangeLen):
        self.delta = desti-source
        self.sourceStart = source
        self.sourceEnd = source + rangeLen-1

    def isNumberInRange(self, number):
        return self.sourceStart <= number <= self.sourceEnd
        
    def convertNumber(self, number):
        if self.sourceStart <= number <= self.sourceEnd:
            return number + self.delta
        return -1

data = []
with open("data.txt") as f:
    for line in f:
        if line == "\n":
            continue
            
        data.append(line.strip().split())

seeds = [int(seedNumber) for seedNumber in data[0][1:]]
allMaps = []
map = []

for i in range(3, len(data)):
    if data[i][0].isdigit():
        map.append(Mapping(*[int(x) for x in data[i]]))
    else:
        allMaps.append(map)
        map = []

allMaps.append(map)

for table in allMaps:
    for i in range(len(seeds)):
        for mapping in table:
            if mapping.isNumberInRange(seeds[i]):
                seeds[i] = mapping.convertNumber(seeds[i])
                break

print(min(seeds))