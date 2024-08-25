from collections import defaultdict
from itertools import cycle

adjDict = defaultdict(list)
with open("data.txt") as f:
    directions = list(f.readline().strip())
    f.readline()
    
    for line in f:
        adjDict[line[0:3]] = [line[7:10], line[12:15]]

cur = "AAA"
count = 0
for direction in cycle(directions):
    if cur == "ZZZ":
        print(count)
        break

    if direction == "L":
        cur = adjDict[cur][0]
    else:
        cur = adjDict[cur][1]
    count += 1
