from collections import Counter

groups = []

with open("data.txt") as f:
    currentGroup = ""
    numberOfPeople = 0

    for line in f:
        if line == "\n":
            groups.append([x for x, y in Counter(currentGroup).items() if y == numberOfPeople])
            currentGroup = ""
            numberOfPeople = 0
        else:
            currentGroup += line.strip()
            numberOfPeople += 1

    groups.append([x for x, y in Counter(currentGroup).items() if y == numberOfPeople])

print(sum(len(x) for x in groups))