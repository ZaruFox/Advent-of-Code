from collections import defaultdict
import heapq

requires = defaultdict(list)
leadsTo = defaultdict(list)
with open('data.txt') as f:
    for line in f:
        requires[line[36]].append(line[5])
        leadsTo[line[5]].append(line[36])

startingChar = (leadsTo.keys() - requires.keys()).pop()

heap = [startingChar]
visited = set()
res = ""

while heap:
    char = heapq.heappop(heap)

    if char in visited:
        continue
    visited.add(char)

    for nextChar in leadsTo[char]:
        if all(x in visited for x in requires[nextChar]):
            heapq.heappush(heap, nextChar)

    res += char

print(res)
