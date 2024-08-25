groups = []

with open("data.txt") as f:
    currentGroup = set()

    for line in f:
        if line == "\n":
            groups.append(currentGroup)
            currentGroup = set()
        else:
            currentGroup |= set(line.strip())

    groups.append(currentGroup)

print(sum(len(x) for x in groups))