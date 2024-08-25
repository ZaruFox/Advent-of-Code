from collections import Counter

boxes = []
with open("data.txt") as f:
    for line in f:
        boxes.append(Counter(line.strip()))

two = 0
three = 0
for box in boxes:
    if any(x == 3 for x in box.values()):
        three += 1
    if any(x == 2 for x in box.values()):
        two += 1
print(two*three)