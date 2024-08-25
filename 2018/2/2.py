from collections import Counter
from sys import exit

boxes = []
with open("data.txt") as f:
    for line in f:
        boxes.append(line.strip())

for box1 in boxes:
    for box2 in boxes:
        diff = []
        for i in range(len(box1)):
            if box1[i] != box2[i]:
                diff.append(i)

        if len(diff) == 1:
            print(box1[:diff[0]] + box1[diff[0]+1:])
            exit()
