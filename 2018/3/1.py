import re

squares = []

with open("data.txt") as f:
    for line in f:
        squareData = re.split(r" @ |,|: |x", line.strip().lstrip("#"))
        squareData = [int(x) for x in squareData]
        squares.append(squareData)

used = set()
overlaps = set()
for id_, x, y, width, height in squares:
    for newX in range(x, x+width):
        for newY in range(y, y+height):
            if (newX, newY) in used:
                overlaps.add((newX, newY))
            else:
                used.add((newX, newY))

print(len(overlaps))
