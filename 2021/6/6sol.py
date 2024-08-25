with open("6data.txt") as f:
    data = [int(x) for x in f.readline().strip().split(",")]

ageRecord = {}

for i in data:
    if i in ageRecord.keys():
        ageRecord[i] += 1
    else:
        ageRecord[i] = 1

#change according to part
for _ in range(256):
    newRecord = {}
    for key, value in ageRecord.items():
        if key == 0:
            newRecord[8] = value
            try:
                newRecord[6] += value
            except KeyError:
                newRecord[6] = value
        else:
            try:
                newRecord[key-1] += value
            except KeyError:
                newRecord[key-1] = value
        

    ageRecord = newRecord

print(sum(ageRecord.values()))