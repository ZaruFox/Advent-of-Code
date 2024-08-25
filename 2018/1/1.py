res = 0
with open("data.txt") as f:
    for line in f:
        res += int(line.strip())
print(res)