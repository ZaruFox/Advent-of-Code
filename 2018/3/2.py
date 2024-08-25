import re
import collections

squares = []

with open("data.txt") as f:
    for line in f:
        squareData = re.split(r" @ |,|: |x", line.strip().lstrip("#"))
        squareData = [int(x) for x in squareData]
        squares.append(squareData)

used = {}
idWithoutOverflow = set([data[0] for data in squares])
for id_, x, y, width, height in squares:
    for newX in range(x, x+width):
        for newY in range(y, y+height):
            if (newX, newY) in used:
                idWithoutOverflow.discard(id_)
                idWithoutOverflow.discard(used[(newX, newY)])
            else:
                used[(newX, newY)] = id_


print(idWithoutOverflow.pop())
