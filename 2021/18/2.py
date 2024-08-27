import collections
import math

def explode(number):
    stack = collections.deque([(2, number, 0), (2, number, 1)])
    prevNumber = None
    explodedPair = None

    while stack:
        depth, parent, i = stack.popleft()
        pair = parent[i]

        if type(pair) == int:
            if explodedPair:
                parent[i] += explodedPair[0][explodedPair[1]][1]
                explodedPair[0][explodedPair[1]] = 0
                return True

            prevNumber = (parent, i)

        elif depth == 5 and not explodedPair:
            explodedPair = (parent, i)

            if prevNumber:
                prevNumber[0][prevNumber[1]] += pair[0]

        else:
            stack.appendleft((depth+1, pair, 1))
            stack.appendleft((depth+1, pair, 0))

    if explodedPair:
        explodedPair[0][explodedPair[1]] = 0
        return True
    return False

def split(pair):
    for i in (0, 1):
        if type(pair[i]) == list:
            if split(pair[i]):
                return True

        elif pair[i] > 9:
            pair[i] = [pair[i]//2, math.ceil(pair[i]/2)]
            return True

    return False


def findMagnitude(pair):
    if type(pair) == int:
        return pair

    return findMagnitude(pair[0])*3 + findMagnitude(pair[1])*2

def reduce(pair):
    while True:
        if not (explode(pair) or split(pair)):
            break

data = []

with open("data.txt") as f:
    for line in f:
        data.append(line.strip())

res = 0
for i in range(len(data)):
    for j in range(len(data)):
        pair = [eval(data[i]), eval(data[j])]
        reduce(pair)
        res = max(res, findMagnitude(pair))
print(res)