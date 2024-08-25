from functools import cache

adapters = [0]
with open("data.txt") as f:
    for line in f:
        adapters.append(int(line.strip()))
adapters.append(max(adapters)+3)
adapters.sort()

@cache
def dp(i):
    if i == len(adapters)-1:
        return 1

    total = 0
    for j in range(i+1, i+4):
        if j < len(adapters) and adapters[j] - adapters[i] <= 3:
            total += dp(j)
    return total

print(dp(0))