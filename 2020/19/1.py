rules = {}
messages = []

with open("data.txt") as f:
    for line in f:
        if line == "\n":
            break

        key, values = line.strip().split(": ")
        if "\"" in values:
            rules[int(key)] = values[1]
            continue
            
        values = values.split(" | ")
        rules[int(key)] = [[int(y) for y in x.split(" ")] for x in values]

    for line in f:
        messages.append(line.strip())

def solve(message, i, ruleNumber):
    if rules[ruleNumber] in ("a", "b"):
        return (message[i] == rules[ruleNumber], i+1)
        
    for choice in rules[ruleNumber]:
        ruleValid = True
        newI = i
        for nextRule in choice:
            x, newI = solve(message, newI, nextRule)
            if not x:
                ruleValid = False
                break

        if ruleValid:
           return (True, newI)
    return (False, -1)

res = 0
for message in messages:
    valid, i = solve(message, 0, 0)
    if valid and i == len(message):
        res += 1
print(res)