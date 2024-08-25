from collections import defaultdict
import heapq

requires = defaultdict(list)
leadsTo = defaultdict(list)
with open('data.txt') as f:
    for line in f:
        requires[line[36]].append(line[5])
        leadsTo[line[5]].append(line[36])

startingChar = (leadsTo.keys() - requires.keys()).pop()
total = set(leadsTo.keys()).union(set(requires.keys()))

heap = [startingChar]
finished = set()
workingOn = set()
timeTaken = 0
workers = [(0, "")] * 5

while len(finished) != len(total):
    print(workers, heap, finished, timeTaken)
    if heap:
        char = heapq.heappop(heap)
        if char in workingOn:
            continue
        workingOn.add(char)

        workerIndex = min(range(len(workers)), key= lambda x: workers[x][0])
        if workers[workerIndex][1] != "":
            timeTaken, characterFinished = workers[workerIndex]
            workers[workerIndex] = (timeTaken + ord(char)-ord("A")+61, char)
        else:
            workers[workerIndex] = (timeTaken + ord(char)-ord("A")+61, char)
            continue

    else:
        workerIndex = None
        for i in range(len(workers)):
            if workers[i][1] == "":
                continue

            if workerIndex is None or workers[workerIndex][0] > workers[i][0]:
                workerIndex = i
            
        timeTaken, characterFinished = workers[workerIndex]
        workers[workerIndex] = (0, '')


    finished.add(characterFinished)
    for nextChar in leadsTo[characterFinished]:
        if all(x in finished for x in requires[nextChar]):
            heapq.heappush(heap, nextChar)

print(timeTaken)
    
