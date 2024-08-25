from collections import Counter

WIDTH = 25
HEIGHT = 6

layersList = []
with open("data.txt") as f:
    data = [int(x) for x in f.readline().strip()]

for i in range(0, len(data), WIDTH*HEIGHT):
    layer = []
    for j in range(i, i+WIDTH*HEIGHT, WIDTH):
        layer.append(data[j:j+WIDTH])
    layersList.append(layer)

minZero = 99999
res = 0

for layer in layersList:
    count = Counter(sum(layer, []))
    if count[0] < minZero:
        minZero = count[0]
        res = count[1] * count[2]

print(res)