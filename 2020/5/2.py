passes = []

with open("data.txt") as f:
    for line in f:
        passes.append([line[:7], line[7:10]])

allIDs = []
for rowPath, columnPath in passes:
    rowMin = 0
    rowMax = 127

    for direction in rowPath:
        mid = (rowMin + rowMax) // 2
        if direction == "F":
            rowMax = mid
        else:
            rowMin = mid + 1

    columnMin = 0
    columnMax = 7
    for direction in columnPath:
        mid = (columnMin + columnMax) // 2
        if direction == "L":
            columnMax = mid
        else:
            columnMin = mid + 1

    allIDs.append(columnMin + rowMin * 8)

allIDs = set(allIDs)
for i in range(1001):
    if (i not in allIDs) and (i-1 in allIDs) and (i+1 in allIDs):
        print(i)
        break