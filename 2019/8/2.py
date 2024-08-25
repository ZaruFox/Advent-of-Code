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

finalImage = ""
for y in range(HEIGHT):
    for x in range(WIDTH):
        for i in range(len(layersList)):
            if layersList[i][y][x] == 1:
                finalImage += "#"
                break
            elif layersList[i][y][x] == 0:
                finalImage += " "
                break
    finalImage += "\n"

print(finalImage)