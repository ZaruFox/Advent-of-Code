# 8: 42 | 42 8
# 11: 42 31 | 42 11 31

# 42: b (a 90 | b 20) | a 132
# 31: b 65 | a 13

# 105: "b"  23: "a"

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


def findMatching(rule):
    if rules[rule] in ("a", "b"):
        return [rules[rule]]

    res = []
    for choice in rules[rule]:
        matches = findMatching(choice[0])
        for nextRule in choice[1:]:
            newMatching = []
            for x in matches:
                for y in findMatching(nextRule):
                    newMatching.append(x+y)
            matches = newMatching
        res += matches
    return res

match42 = set(findMatching(42))
match31 = set(findMatching(31))

def solve(message, i, ruleNumber):
    if rules[ruleNumber] in ("a", "b"):
        return [i+1] if rules[ruleNumber] == message[i] else []

    res = []
    if ruleNumber == 8:
        while i+8 <= len(message) and message[i:i+8] in match42:
            res.append(i+8)
            i += 8
        return res

    if ruleNumber == 11:
        n = 1
        while i + n*11 <= len(message):
            valid = True
            for j in range(1, n+1):
                if not (message[i+(j-1)*8:i+j*8] in match42 and message[i+n*8+(j-1)*8:i+n*8+j*8] in match31):
                    valid = False
                    break

            if valid:
                res.append(i + n*16)
            n += 1
        return res
                    

    for choice in rules[ruleNumber]:
        possibleMatches = [i]
        for nextRule in choice:
            tmp = []
            for j in possibleMatches:
                tmp += solve(message, j, nextRule)
            possibleMatches = tmp
        res += possibleMatches

    return res

res = 0
for message in messages:
    i = solve(message, 0, 0)
    if len(message) in i:
        res += 1
print(res)