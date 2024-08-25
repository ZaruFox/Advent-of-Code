import re

bagRules = {}

with open("data.txt") as f:
    for line in f:
        rule = re.split(r" bags? contain | bags?[,.] ?", line.strip())[:-1]
        
        bagRules[rule[0]] = []
        if rule[1] != "no other":
            for bagDescription in rule[1:]:
                bagRules[rule[0]].append((int(bagDescription[0]), bagDescription[2:]))


def dfs(cur):
    if cur == "shiny gold":
        return True
    return any(dfs(nextBag) for count, nextBag in bagRules[cur])

res = 0
for startingBag in bagRules:
    if startingBag != "shiny gold" and dfs(startingBag):
        res += 1

print(res)

    