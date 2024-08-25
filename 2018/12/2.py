from collections import defaultdict

rules = {}
currentState = set()

with open("data.txt") as f:
    tmp = list(f.readline().lstrip("initial state: ").rstrip())
    for i in range(len(tmp)):
        if tmp[i] == "#":
            currentState.add(i)

    f.readline()

    for line in f:
        rule, result = line.strip().split(" => ") 
        rules[rule] = result

visited = {}
target = None
for cycle in range(1000):
    minValue = min(currentState)
    normalized = tuple([x-minValue for x in currentState])
    if normalized in visited and (target is None or target == normalized):
        target = normalized
        print(minValue, cycle)
        print(cycle - visited[normalized])
    visited[normalized] = cycle


    newState = set()
    for targetPot in currentState:
        for currentPot in range(targetPot-2, targetPot+3):
            tmp = ""
            for adjPot in range(currentPot-2, currentPot+3):
                if adjPot in currentState:
                    tmp += "#"
                else:
                    tmp += "."

            if rules[tmp] == "#":
                newState.add(currentPot)
    
    currentState = newState 

print(sum([x for x in target]) + len(target) * (50000000000 - 86))
        