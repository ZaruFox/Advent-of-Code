import re
from collections import defaultdict


records = []
with open("data.txt") as f:
    for line in f:
        records.append(line.strip())

records.sort()

# parse records
parsedRecords = []
curGuard = None

for record in records:
    record = re.split(r"-|] | |:", record.lstrip("["))
    
    if record[-1] == "shift":
        curGuard = int(record[6].lstrip("#"))
    parsedRecords.append((curGuard, int(record[4]), record[-1]))

timeAsleep = defaultdict(lambda : [0] * 60)
for i in range(len(parsedRecords)):
    if parsedRecords[i][2] == "up":
        for minute in range(parsedRecords[i-1][1], parsedRecords[i][1]):
            timeAsleep[parsedRecords[i][0]][minute] += 1

maxTime = 0
res = None
for guard, timeData in timeAsleep.items():
    tmp = max(range(60), key = lambda x: timeData[x])
    if timeData[tmp] > maxTime:
        maxTime = tmp
        res = guard * tmp
print(res)