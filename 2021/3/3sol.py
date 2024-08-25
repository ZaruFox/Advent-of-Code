#part 1
data = []
with open("3data.txt") as f:
    for row in f:
        data.append(row.strip())

max_ = ""
min_ = ""

for i in range(len(data[0])):
    counter = 0
    for j in range(len(data)):
        if data[j][i] == "0":
            counter += 1

    if counter > 500:
        max_ += "0"
        min_ += "1"

    else:
        max_ += "1"
        min_ += "0"


print(int(max_, 2) * int(min_, 2))

#part 2
data2 = data.copy()

j = 0
while len(data2) != 1:
    counter = 0
    for k in range(len(data2)):
        if data2[k][j] == "0":
            counter += 1

    if counter > len(data2) // 2:
        max2 = "0"
    else:
        max2 = "1"
    
    i = 0
    
    while i < len(data2):
        if data2[i][j] != max2:
            data2.pop(i)
        else:
            i += 1

    j += 1

data3 = data.copy()

j = 0
while len(data3) != 1:
    counter = 0
    for k in range(len(data3)):
        if data3[k][j] == "0":
            counter += 1

    if counter > len(data3) // 2:
        min2 = "1"
    else:
        min2 = "0"

    
    i = 0
    while i < len(data3):
        if data3[i][j] != min2:
            data3.pop(i)
        else:
            i += 1

    j += 1
print(data2, data3)
print(int(data3[0], 2) * int(data2[0], 2))