from collections import Counter

adapters = [0]
with open("data.txt") as f:
    for line in f:
        adapters.append(int(line.strip()))
adapters.append(max(adapters)+3)
adapters.sort()

differenceCount = Counter([adapters[i] - adapters[i-1] for i in range(1, len(adapters))])
print(differenceCount[1] * differenceCount[3])