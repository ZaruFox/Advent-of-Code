with open("data.txt") as f:
    modules = [int(x.strip()) for x in f]

print(sum([(x//3) - 2 for x in modules]))