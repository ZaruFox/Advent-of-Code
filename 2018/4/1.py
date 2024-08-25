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

timeAsleep = defaultdict(int)
for i in range(len(parsedRecords)):
    if parsedRecords[i][2] == "up":
        timeAsleep[parsedRecords[i][0]] += parsedRecords[i][1] - parsedRecords[i-1][1]

mostSleep = max(timeAsleep.keys(), key = lambda x: timeAsleep[x])
minutesSlept = [0] * 60
for i in range(len(parsedRecords)):
    if parsedRecords[i][2] == "up" and parsedRecords[i][0] == mostSleep:
        for minute in range(parsedRecords[i-1][1], parsedRecords[i][1]):
            minutesSlept[minute] += 1

print(mostSleep * max(range(60), key = lambda x: minutesSlept[x]))