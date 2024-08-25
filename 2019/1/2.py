with open("data.txt") as f:
    modules = [int(x.strip()) for x in f]

res = 0
for fuel in modules:
    while fuel//3 - 2 > 0:
        fuel = fuel // 3 - 2
        res += fuel

print(res)