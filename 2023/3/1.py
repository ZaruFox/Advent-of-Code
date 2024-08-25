def checkForSymbols(data, x, y):
    for x2, y2 in [(x-1,y-1),(x-1, y), (x-1,y+1), 
                   (x,y-1), (x,y+1), 
                   (x+1,y-1), (x+1,y), (x+1,y+1)]:
        if (not data[y2][x2].isdigit()) and data[y2][x2] != ".":
            return True
    return False

data = []
with open("data.txt") as f:
    for line in f:
        data.append("." + line.strip() + ".")
data.insert(0, "."*len(data[0]))
data.append("."*len(data[0]))

res = 0
for y in range(len(data)):
    x = 0
    while x < len(data):
        if data[y][x].isdigit():
            number = ""
            valid = False
            
            while data[y][x].isdigit():
                number += data[y][x]
                if not valid and checkForSymbols(data, x, y):
                    valid = True
                x += 1

            if valid:
                res += int(number)
        x += 1
print(res)