import functools

@functools.cache
def findArrangements(gears, groups, i):
    if len(gears)-i < len(groups)+sum(groups)-1:
        return 0

    if not groups:
        if "#" in gears[i:]:
            return 0
        return 1
        
    total = 0
    if gears[i] in ("#", "?"):
        if not "." in gears[i:i+groups[0]] and (i+groups[0] == len(gears) or gears[i+groups[0]] != "#"):
            total += findArrangements(gears, groups[1:], i+1+groups[0])
            

    if gears[i] in (".", "?"):
        total += findArrangements(gears, groups, i+1)
        

    return total


res = 0

with open("data.txt") as f:
    for line in f:
        gears, groups = line.strip().split()
        groups = [int(x) for x in groups.split(",")]*5
        gears = "?".join([gears]*5)
        res += findArrangements(tuple(gears), tuple(groups), 0)
        
print(res)