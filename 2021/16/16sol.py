from collections import deque
import numpy


data = ""
with open("16data.txt") as f:
    for char in f.readline().strip():
        data += bin(int(char, 16))[2:].zfill(4)
        
i = 0
res = 0
while i+6 < len(data):
    res += int(data[i:i+3], 2)
    i += 3

    if int(data[i:i+3], 2) == 4:
        i += 3
        while data[i] == "1":
            i += 5
        i += 5

    else:
        i += 3
        if data[i] == "0":
            i += 1
            i += 15
            continue
        elif data[i] == "1":
            i += 12
            continue

print(res)

# part 2
data = ""
with open("16data.txt") as f:
    for char in f.readline().strip():
        data += bin(int(char, 16))[2:].zfill(4)

print(data[-100:], len(data))
def parse(packet, prevTypeID, numberOfPackets = 99999999999):
    res = []
    i = 0
    while i < len(packet) and numberOfPackets > 0 and len(set(packet[i:])) == 2:
        typeID = int(packet[i+3:i+6], 2)
        i += 6
        
        if typeID == 4:
            x = ""
            while packet[i] == "1":
                x += packet[i+1:i+5]
                i += 5

            x += packet[i+1:i+5]
            i += 5
            numberOfPackets -= 1
            res.append(int(x, 2))

        else:
            lengthTypeID = packet[i]
            i += 1
            
            if lengthTypeID == "0":
                length = int(packet[i:i+15], 2)
                subStringRes, newIndex = parse(packet[i+15:i+15+length], typeID)
                i += 15


            else:
                subStringRes, newIndex = parse(packet[i+11:], typeID, int(packet[i:i+11], 2))
                i += 11

            res.append(subStringRes)
            i += newIndex
            numberOfPackets -= 1
            

    if prevTypeID == None:
        return [res, i]
    elif prevTypeID == 0:
        return [sum(res), i]
    elif prevTypeID == 1:
        return [numpy.prod(res), i]
    elif prevTypeID == 2:
        return [min(res), i]
    elif prevTypeID == 3:
        return [max(res), i]
    elif prevTypeID == 5:
        return [int(res[0] > res[1]), i]
    elif prevTypeID == 6:
        return [int(res[0] < res[1]), i]
    elif prevTypeID == 7:
        return [int(res[0] == res[1]), i]

print(parse(data, None))
                