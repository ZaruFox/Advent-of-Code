with open("data.txt") as f:
    cardKey = int(f.readline().strip())
    doorKey = int(f.readline().strip())

def transform(subject, loopSize):
    res = 1
    for i in range(loopSize):
        res *= subject
        res %= 20201227
    return res

def findLoopSize(subject, target):
    res = 1
    loopSize = 0
    while res != target:
        res *= 7
        res %= 20201227
        loopSize += 1
    return loopSize

print(transform(doorKey, findLoopSize(7, cardKey)))