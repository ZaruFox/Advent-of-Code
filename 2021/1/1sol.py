data = []
res = 0

with open("1data.txt") as f:
    for line in f:
        data.append(line.strip())
data = [int(x) for x in data]

prev = None
for i in range(2, len(data)):
    cur = data[i-2] + data[i-1] + data[i]
    if prev != None and cur > prev:
        res += 1
    prev = cur

print(res)
        