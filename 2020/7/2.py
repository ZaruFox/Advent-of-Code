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
    return sum([(dfs(nextBag)+1)*count for count, nextBag in bagRules[cur]])

print(dfs("shiny gold"))

