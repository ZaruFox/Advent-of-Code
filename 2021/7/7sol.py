import numpy

with open("7data.txt") as f:
    data = [int(x) for x in f.readline().strip().split(",")]

res = 9999999999999999999999999

for i in range(0, 3000):
    temp = 0
    for num in data:
        temp += abs(num - i)

    res = min(temp, res)

print(res)

#part 2

with open("7data.txt") as f:
    data = [int(x) for x in f.readline().strip().split(",")]

res = 9999999999999999999999999

for i in range(0, 3000):
    temp = 0
    for num in data:
        temp += (1 + abs(num - i)) * abs(num - i) / 2

    res = min(temp, res)

print(res)