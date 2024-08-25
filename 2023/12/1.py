
def findArrangements(gears, groups, i, count):
    if i == len(gears):
        if len(groups) == 1 and count == groups[0]:
            return 1
        return 0 if groups else 1
        
    total = 0
    if gears[i] in ("#", "?") and groups and count < groups[0]:
        total += findArrangements(gears, groups, i+1, count+1)
    
    if gears[i] in (".", "?"):
        if count == 0 or not groups:
            total += findArrangements(gears, groups, i+1, 0)
        elif count == groups[0]:
            tmp = groups.pop(0)
            total += findArrangements(gears, groups, i+1, 0)
            groups.insert(0, tmp)
        
    return total


res = 0

with open("data.txt") as f:
    for line in f:
        gears, groups = line.strip().split()
        groups = [int(x) for x in groups.split(",")]

        res += findArrangements(gears, groups, 0, 0)

print(res)