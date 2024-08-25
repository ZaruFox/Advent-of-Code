from collections import defaultdict

rules = {}
currentState = defaultdict(lambda: ".")

with open("data.txt") as f:
    tmp = list(f.readline().lstrip("initial state: ").rstrip())
    for i in range(len(tmp)):
        currentState[i] = tmp[i]

    f.readline()

    for line in f:
        rule, result = line.strip().split(" => ") 
        rules[rule] = result

for cycle in range(20):
    newState = defaultdict(lambda: ".")
    for currentPot in range(min(currentState.keys())-2, max(currentState.keys()) + 3):
        tmp = ""
        for adjPot in range(currentPot-2, currentPot+3):
            tmp += currentState[adjPot]

        if rules[tmp] == "#":
            newState[currentPot] = "#"
    
    currentState = newState 

print(sum([x for x in currentState.keys()]))
        