# ==================== PRINT HELPER  ==================
import time
import re, sys

class Reprinter:
    def __init__(self):
        self.text = ''

    def moveup(self, lines):
        for _ in range(lines):
            sys.stdout.write("\x1b[A")

    def reprint(self, text):
        # Clear previous text by overwritig non-spaces with spaces
        self.moveup(self.text.count("\n"))
        sys.stdout.write(re.sub(r"[^\s]", " ", self.text))

        # Print new text
        lines = min(self.text.count("\n"), text.count("\n"))
        self.moveup(lines)
        sys.stdout.write(text)
        self.text = text

from collections import defaultdict

tree = set()
lumberyard = set()

with open("data.txt") as f:
    data = f.read().splitlines()

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "|":
            tree.add((x, y))
        elif data[y][x] == "#":
            lumberyard.add((x, y))


printer = Reprinter()
for cycle in range(100000):
    treeCount = defaultdict(int)
    lumberCount = defaultdict(int)

    for x, y in tree:
        for adj in [(x+1,y-1), (x, y-1), (x-1, y-1), (x+1, y), (x-1, y), (x+1, y+1), (x, y+1), (x-1, y+1)]:
            treeCount[adj] += 1

    for x, y in lumberyard:
        for adj in [(x+1,y-1), (x, y-1), (x-1, y-1), (x+1, y), (x-1, y), (x+1, y+1), (x, y+1), (x-1, y+1)]:
            lumberCount[adj] += 1

    for x, y in treeCount.keys() | lumberCount.keys() | tree | lumberyard:
        if not (0 <= x < len(data[0]) and 0 <= y < len(data)):
            continue

        if ((x, y) not in tree and (x, y) not in lumberyard) and treeCount[(x, y)] >= 3:
            tree.add((x, y))

        elif (x, y) in tree and lumberCount[(x, y)] >= 3:
            tree.discard((x, y))
            lumberyard.add((x, y))

        elif (x, y) in lumberyard and not (treeCount[(x, y)] >= 1 and lumberCount[(x, y)] >= 1):
            lumberyard.discard((x, y))

    grid = ""
    for y in range(len(data)):
        for x in range(len(data[0])):
            if (x, y) in tree:
                grid += "|"
            elif (x, y) in lumberyard:
                grid += "#"
            else:
                grid += "."
        grid += "\n"
    printer.reprint(grid[:-1])
    time.sleep(0.01)



print(len(lumberyard) * len(tree))