from heapq import heappop, heappush
from collections import defaultdict
from math import inf

depth = 11109
target = (9,731)

erosionLevel = [[0] * (target[0]+1000) for _ in range(target[1]+501)]

for y in range(len(erosionLevel)):
    for x in range(len(erosionLevel[0])):
        if (x, y) == (0, 0) or (x, y) == target:
            index = 0
        elif y == 0:
            index = x * 16807
        elif x == 0:
            index = y * 48271
        else:
            index = erosionLevel[y][x-1] * erosionLevel[y-1][x]

        erosionLevel[y][x] = (index + depth) % 20183

groundType = [[level % 3 for level in row] for row in erosionLevel]

VALIDSTATES = {0: {0, 1}, 1: {1, 2}, 2: {0, 2}}

heap = [(0, 0, 0, 0)]
visited = defaultdict(lambda : inf)
visited[(0, 0, 0)] = 0

while heap:
    cost, x, y, state = heappop(heap)

    if (x, y, state) == (target[0], target[1], 0):
        print(cost)
        break

    otherState = (VALIDSTATES[groundType[y][x]] ^ {state,}).pop()
    if cost + 7 < visited[(x, y, otherState)]:
        visited[(x, y, otherState)] = cost + 7
        heappush(heap, (cost+7, x, y, otherState))

    for adjX, adjY in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if adjX < 0 or adjY < 0 or state not in VALIDSTATES[groundType[adjY][adjX]]:
            continue

        if cost + 1 >= visited[(adjX, adjY, state)]:
            continue
        visited[(adjX, adjY, state)] = cost + 1
        heappush(heap, (cost+1, adjX, adjY, state))







        